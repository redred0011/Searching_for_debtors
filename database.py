from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database engine
engine = create_engine('sqlite:///Customers.db', echo=True)

# Initialize the base class
Base = declarative_base()

# Define the table model
class Customer(Base): 
    __tablename__ = 'Customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String) 
    e_mail = Column(String)  
    number_bank_statement = Column(String)  
    
# Create the table in the database
Base.metadata.create_all(engine)

# Create a session class
Session = sessionmaker(bind=engine)

def add_customer():
    
    # Add a customer to the database
    session = Session()
    list_customers()
    name = input("Enter name:")
    number_phone = input("Enter phone number:")
    e_mail = input("Enter email:")
    number_bank_statement = input("Enter bank account number as it appears in the CSV file:")
    
    customer = Customer(name=name, number_phone=number_phone, e_mail=e_mail, number_bank_statement=number_bank_statement) 
    session.add(customer)
    session.commit()
    session.close()
    print("Added office customer")   
    

def delete_customer():
    # Delete a customer from the database
    session = Session()
    list_customers()
    customer_id = input("Enter the ID of the customer you want to delete:")
    
    customer = session.query(Customer).filter_by(id=customer_id).first()
    
    if customer:
        session.delete(customer)
        session.commit()
        session.close()
        print("Deleted office customer with ID:", customer_id)
    else:
        session.close()
        print("Customer with specified ID does not exist.")

def list_customers():
    # List all customers in the database
    session = Session()
    customers = session.query(Customer).all()
    
    if not customers:
        print("No customers available.")
    else:
        print("List of available customers:")
        for customer in customers:
            print(f"ID: {customer.id}, Name: {customer.name}, Phone Number: {customer.number_phone}, Email: {customer.e_mail}, Bank Account Number: {customer.number_bank_statement}")

def update_customer():
    # Update a customer's information in the database
    session = Session()
    list_customers()
    customer_id = input("Enter the ID of the customer whose information you want to update:")

    customer = session.query(Customer).filter_by(id=customer_id).first()

    if customer:
        print("Choose a field to update:")
        print("1. Name")
        print("2. Phone Number")
        print("3. Email")
        print("4. Bank Account Number")
        choice = input("Your choice (1/2/3/4):")

        if choice == "1":
            new_name = input("New name:")
            customer.name = new_name
        elif choice == "2":
            new_number_phone = input("New phone number:")
            customer.number_phone = new_number_phone
        elif choice == "3":
            new_e_mail = input("New email:")
            customer.e_mail = new_e_mail
        elif choice == "4":
            new_number_bank_statement = input("New bank account number:")
            customer.number_bank_statement = new_number_bank_statement
        else:
            print("Invalid choice.")

        session.commit()
        session.close()
        print("Updated customer information with ID:", customer_id)
    else:
        session.close()
        print("Customer with specified ID does not exist.")


def main():
    
    choose = input("Add - D , Delete - U , Update - Z:").lower()

    if choose == "d":
        
        add_customer()
    
    elif choose == "u":
        
        delete_customer()
    
    elif choose == "z":
        
        update_customer()
    
    else:
        main()
