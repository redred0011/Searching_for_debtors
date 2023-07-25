from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import pywhatkit as kit
import datetime
import docx
import time

# Create a database engine and a session factory
engine = create_engine('sqlite:///debtors.db')
Session = sessionmaker(bind=engine)

# Define the Debtor class
Base = declarative_base()

class Debtor(Base):
    __tablename__ = 'Debtors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_phone = Column(String)
    e_mail = Column(String)
    number_bank_statement = Column(String)

def get_all_phone_numbers():
    # Create a new session
    session = Session()

    # Query the database for all phone numbers
    phone_numbers = session.query(Debtor.number_phone).all()

    # Close the session
    session.close()

    # Return the list of phone numbers
    return [phone_number[0] for phone_number in phone_numbers]

def read_docx_file(file_path):
    # Create a Document object
    doc = docx.Document(file_path)

    # Extract the text from the document
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    # Return the text
    return text

def main():
    # Get the list of phone numbers from the database
    phone_numbers = get_all_phone_numbers()

    # Set the path to the .docx file
    file_path = "prośba.docx"

    # Read the text from the .docx file
    message = read_docx_file(file_path)

    # Wait for WhatsApp Web to open (increase the initial wait time to 30 seconds)
    time.sleep(30)

    # Send the message to all phone numbers
    for phone_number in phone_numbers:
        if not phone_number.startswith("+"):
            print(f"Skipping invalid phone number: {phone_number}")
            continue

        # Get the current hour and minute
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        # Send the message with a delay of 1 minute and 15 seconds
        kit.sendwhatmsg(phone_number, message, current_hour, current_minute + 1, 15)


