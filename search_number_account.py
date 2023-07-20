from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

# Tworzenie silnika bazy danych dla Customers
customers_engine = create_engine('sqlite:///Customers.db', echo=True)

# Inicjalizacja klasy bazowej dla Customers
BaseCustomers = declarative_base()

# Definicja modelu tabeli dla Customers
class Customer(BaseCustomers): 
    __tablename__ = 'Customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String) 
    e_mail = Column(String)  
    number_bank_statement = Column(String)  
    
# Tworzenie tabeli w bazie danych dla Customers
BaseCustomers.metadata.create_all(customers_engine)

# Tworzenie klasy sesji dla Customers
SessionCustomers = sessionmaker(bind=customers_engine)

# Tworzenie silnika bazy danych dla Debtors
debtors_engine = create_engine('sqlite:///Debtors.db', echo=True)

# Inicjalizacja klasy bazowej dla Debtors
BaseDebtors = declarative_base()

# Definicja modelu tabeli dla Debtors
class Debtor(BaseDebtors):
    __tablename__ = 'Debtors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String)
    e_mail = Column(String)
    number_bank_statement = Column(String)

# Tworzenie tabeli w bazie danych dla Debtors
BaseDebtors.metadata.create_all(debtors_engine)

# Tworzenie klasy sesji dla Debtors
SessionDebtors = sessionmaker(bind=debtors_engine)


def get_customer_bank_account(customer_id):
    session = SessionCustomers()
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
            if account_number in row:
                found_rows.append(dict(zip(header, row)))
    return found_rows

def main():
    csv_file = 'bank_statements.csv'

    session = SessionCustomers()
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
            print(f"Nie znaleziono żadnych operacji dla klienta o ID: {customer.id}, Nazwie: {customer.name}, E-mail: {customer.e_mail}")
            accounts_without_transactions.append(customer)

        else:
            print(f"Operacje dla klienta o ID: {customer.id}, nazwie: {customer.name} i numerze konta bankowego: {account_number}")
            for row in found_rows:
                print(row)

    if accounts_without_transactions:
        print("Operacja dla tego kontrahenta nie została znaleziona. Dodawanie do Debtors:")
        session = SessionDebtors()
        for debtor_customer in accounts_without_transactions:
            debtor = Debtor(
                name=debtor_customer.name,
                number_phone=debtor_customer.number_phone,
                e_mail=debtor_customer.e_mail,
                number_bank_statement=debtor_customer.number_bank_statement
            )
            session.add(debtor)
        session.commit()
        session.close()

if __name__ == "__main__":
    main()
