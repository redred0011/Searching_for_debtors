from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv
import sending_mail
# Tworzenie silnika bazy danych
engine = create_engine('sqlite:///Customers.db', echo=True)

# Inicjalizacja klasy bazowej
Base = declarative_base()

# Definicja modelu tabeli
class Customer(Base): 
    __tablename__ = 'Customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String) 
    e_mail = Column(String)  
    number_bank_statement = Column(String)  
    
# Tworzenie tabeli w bazie danych
Base.metadata.create_all(engine)

# Tworzenie klasy sesji
Session = sessionmaker(bind=engine)

def get_customer_bank_account(customer_id):
    session = Session()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    session.close()
    if customer:
        return customer.number_bank_statement
    else:
        return None

def find_transactions_with_account_number(account_number, filename):
    found_rows = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Pomijamy nagłówek
        for row in reader:
            full_row_text = ' '.join(row)  # Łączymy wszystkie pola w wierszu
            if account_number in full_row_text:
                found_rows.append(', '.join(row))
    return found_rows

def main():
    csv_file = 'bank_statements.csv'

    session = Session()
    customers = session.query(Customer).all()
    session.close()

    if not customers:
        print("Brak dostępnych klientów.")
        return

    accounts_without_transactions = []  # Lista przechowująca numery kont, dla których nie znaleziono operacji

    for customer in customers:
        account_number = customer.number_bank_statement
        found_rows = find_transactions_with_account_number(account_number, csv_file)

        if not found_rows:
            print(f"Nie znaleziono żadnych operacji dla klientów:")
            accounts_without_transactions.append(account_number)
        else:
            print(f"Operacje dla klienta o ID: {customer.id}, nazwie: {customer.name} i numerze konta bankowego: {account_number}")
            for row in found_rows:
                print(row)

    if accounts_without_transactions:
        print("Operacja dla tego kontrahenta nie została znaleziona:")
        for account_number in accounts_without_transactions:
             print(f"Id: {customer.id}, Nazwa: {customer.name}, Numer rachunku: {account_number}")
             

if __name__ == "__main__":
    main()
