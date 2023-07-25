import os
import docx
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import getpass

# Create a database engine and table for Debtors
debtors_engine = create_engine('sqlite:///debtors.db')
BaseDebtors = declarative_base()

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

# Function to get a password from the console
def get_hidden_password(prompt="Enter password: "):
    try:
        password = getpass.getpass(prompt)
    except Exception as e:
        print("Error:", e)
        password = None
    return password

# Function to send emails
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # SMTP server settings for Zoho account
        smtp_server = 'smtppro.zoho.com'
        smtp_port = 465

        # Create an email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add the message content (text and/or HTML)
        message.attach(MIMEText(body, 'plain'))

        # Create a connection to the SMTP server
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)

        # Log in to the SMTP server
        server.login(sender_email, sender_password)

        # Send the email message
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Close the connection to the SMTP server
        server.quit()

        print(f"Email sent to {recipient_email}!")

    except Exception as e:
        print(f"Error sending email: {e}")

# Function to get email addresses from the database
def get_all_emails():
    emails = []
    session = SessionDebtors()
    try:
        # Execute a query that retrieves the emails of all customers
        debtors = session.query(Debtor.e_mail).all()

        # Get email addresses as strings
        emails = [email[0] for email in debtors]
    except Exception as e:
        print("Error:", e)
    finally:
        session.close()
    return emails

def read_message_from_file(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    # Email sending data
    current_folder = os.path.dirname(os.path.abspath(__file__))
    sender_email = "#######"  # Zoho account email

    subject = "Request for payment !!!!!!!"
    file_path = os.path.join(current_folder, "prośba.docx")
    body = read_message_from_file(file_path)

    if body:
        # Get password from console (if not already known)
        password = get_hidden_password("Enter password: ")

        # Call function to retrieve customer emails from database
        emails = get_all_emails()

        # Display results
        if emails:
            print("Customer emails:")
            for email in emails:
                print(email)
        else:
            print("Failed to retrieve data from database.")

        # Call function to send email for each email address on the list
        for recipient_email in emails:
            send_email(sender_email, password, recipient_email, subject, body)


