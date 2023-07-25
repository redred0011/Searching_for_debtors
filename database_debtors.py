from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a database engine
engine = create_engine('sqlite:///Debtors.db', echo=True)

# Initialize the base class
Base = declarative_base()

# Define the table model
class Customer(Base):
    __tablename__ = 'Debtors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String)
    e_mail = Column(String)
    number_bank_statement = Column(String)

# Create the table in the database
Base.metadata.create_all(engine)
