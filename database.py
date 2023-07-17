from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

def add_customer():
    
    session = Session()
    list_customers()
    name = input("Wprowadź nazwę:")
    number_phone = input("Wprowadź numer telefonu:")
    e_mail = input("Wprowadź e-mail:")
    number_bank_statement = input("Wprowadź numer konta bankowego tak jak jest zapisany w pliku CSV:")
    
    customer = Customer(name=name, number_phone=number_phone, e_mail=e_mail, number_bank_statement=number_bank_statement) 
    session.add(customer)
    session.commit()
    session.close()
    print("Dodano klienta biura")   
    

def delete_customer():
    session = Session()
    list_customers()
    customer_id = input("Wprowadź ID klienta, którego chcesz usunąć:")
    
    customer = session.query(Customer).filter_by(id=customer_id).first()
    
    if customer:
        session.delete(customer)
        session.commit()
        session.close()
        print("Usunięto klienta biura o ID:", customer_id)
    else:
        session.close()
        print("Klient o podanym ID nie istnieje.")

def list_customers():
    session = Session()
    customers = session.query(Customer).all()
    
    if not customers:
        print("Brak dostępnych klientów.")
    else:
        print("Lista dostępnych klientów:")
        for customer in customers:
            print(f"ID: {customer.id}, Nazwa: {customer.name}, Numer telefonu: {customer.number_phone}, E-mail: {customer.e_mail}, Numer konta bankowego: {customer.number_bank_statement}")


def main():
    
    choose = input("Dodanie czy usunięcie kilenta?(Dodanie - D , Usnunięcie - U):").lower()

    if choose == "d":
        add_customer()
    
    elif choose == "u":
        delete_customer()
    
    else:
        main()




