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

def update_customer():
    session = Session()
    list_customers()
    customer_id = input("Wprowadź ID klienta, którego dane chcesz zaktualizować:")

    customer = session.query(Customer).filter_by(id=customer_id).first()

    if customer:
        print("Wybierz pole do zaktualizowania:")
        print("1. Nazwa")
        print("2. Numer telefonu")
        print("3. E-mail")
        print("4. Numer konta bankowego")
        choice = input("Twój wybór (1/2/3/4):")

        if choice == "1":
            new_name = input("Nowa nazwa:")
            customer.name = new_name
        elif choice == "2":
            new_number_phone = input("Nowy numer telefonu:")
            customer.number_phone = new_number_phone
        elif choice == "3":
            new_e_mail = input("Nowy e-mail:")
            customer.e_mail = new_e_mail
        elif choice == "4":
            new_number_bank_statement = input("Nowy numer konta bankowego:")
            customer.number_bank_statement = new_number_bank_statement
        else:
            print("Nieprawidłowy wybór.")

        session.commit()
        session.close()
        print("Zaktualizowano dane klienta o ID:", customer_id)
    else:
        session.close()
        print("Klient o podanym ID nie istnieje.")


def main():
    
    choose = input("Dodanie - D , Usnunięcie - U , Zmiana danych - Z:").lower()

    if choose == "d":
        
        add_customer()
    
    elif choose == "u":
        
        delete_customer()
    
    elif choose == "z":
        
        update_customer()
    
    else:
        main()

main()


