from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Tworzenie silnika bazy danych
engine = create_engine('sqlite:///Debtors.db', echo=True)

# Inicjalizacja klasy bazowej
Base = declarative_base()

# Definicja modelu tabeli
class Customer(Base):
    __tablename__ = 'Debtors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String)
    e_mail = Column(String)
    number_bank_statement = Column(String)

# Tworzenie tabeli w bazie danych
Base.metadata.create_all(engine)
