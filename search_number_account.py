from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

# Create a database engine for Customers
customers_engine = create_engine('sqlite:///Customers.db', echo=True)

# Initialize the base class for Customers
BaseCustomers = declarative_base()

# Define the table model for Customers
class Customer(BaseCustomers): 
    __tablename__ = 'Customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String) 
    e_mail = Column(String)  
    number_bank_statement = Column(String)  
    
# Create the table in the database for Customers
BaseCustomers.metadata.create_all(customers_engine)

# Create a session class for Customers
SessionCustomers = sessionmaker(bind=customers_engine)

# Create a database engine for Debtors
debtors_engine = create_engine('sqlite:///Debtors.db', echo=True)

# Initialize the base class for Debtors
BaseDebtors = declarative_base()

# Define the table model for Debtors
class Debtor(BaseDebtors):
    __tablename__ = 'Debtors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String)
    e_mail = Column(String)
    number_bank_statement = Column(String)

# Create the table in the database for Debtors
BaseDebtors.metadata.create_all(debtors_engine)

# Create a session class for Debtors
SessionDebtors = sessionmaker(bind=debtors_engine)


def add_customer_if_not_exist(name, number_phone, e_mail, number_bank_statement):
    # Add a customer to the database if they don't already exist
    session = SessionCustomers()
    customer = session.query(Customer).filter_by(name=name, e_mail=e_mail).first()

    if not customer:
        new_customer = Customer(name=name, number_phone=number_phone, e_mail=e_mail, number_bank_statement=number_bank_statement)
        session.add(new_customer)
        session.commit()
    session.close()

def get_customer_bank_account(customer_id):
    # Get the bank account number of a customer from the database
    session = SessionCustomers()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    session.close()

    if customer:
        return customer.number_bank_statement
    else:
        return None

def find_transactions_with_account_number(account_number, filename):
    # Find transactions in a CSV file that match a given account number
    found_rows = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            if account_number in row:
                found_rows.append(dict(zip(header, row)))
    return found_rows

def main():
    csv_file = 'bank_statements.csv'

    # Get all customers from the database
    session = SessionCustomers()
    customers = session.query(Customer).all()
    session.close()

    if not customers:
        print("No customers available.")
        return

    accounts_without_transactions = []  # List to store account numbers that have no transactions

    # Find transactions for each customer's bank account number
    for customer in customers:
        account_number = customer.number_bank_statement
        found_rows = find_transactions_with_account_number(account_number, csv_file)

        if not found_rows:
            print(f"No transactions found for customer with ID: {customer.id}, Name: {customer.name}, Email: {customer.e_mail}")
            accounts_without_transactions.append(customer)

        else:
            print(f"Transactions for customer with ID: {customer.id}, Name: {customer.name}, and Bank Account Number: {account_number}")
            for row in found_rows:
                print(row)

    # Add customers with no transactions to the Debtors table
    if accounts_without_transactions:
        print("No transactions found for this customer. Adding to Debtors:")
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
