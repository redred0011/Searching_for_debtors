import os
import docx
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import getpass

# Tworzenie bazy danych i tabeli dla Debtors
debtors_engine = create_engine('sqlite:///debtors.db')
BaseDebtors = declarative_base()

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

# Funkcja do pobrania hasła z konsoli
def get_hidden_password(prompt="Enter password: "):
    try:
        password = getpass.getpass(prompt)
    except Exception as e:
        print("Wystąpił błąd:", e)
        password = None
    return password

# Funkcja do wysyłania emaili
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Ustawienia serwera SMTP dla konta Zoho
        smtp_server = 'smtppro.zoho.com'
        smtp_port = 465

        # Tworzenie wiadomości email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Dodawanie treści wiadomości (tekst i/lub HTML)
        message.attach(MIMEText(body, 'plain'))

        # Utworzenie połączenia z serwerem SMTP
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)

        # Logowanie do serwera SMTP
        server.login(sender_email, sender_password)

        # Wysłanie wiadomości email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Zamknięcie połączenia z serwerem SMTP
        server.quit()

        print(f"Wiadomość email została wysłana na {recipient_email}!")

    except Exception as e:
        print(f"Błąd podczas wysyłania wiadomości email: {e}")

# Funkcja do pobierania adresów email z bazy danych
def get_all_emails():
    emails = []
    session = SessionDebtors()
    try:
        # Wykonanie zapytania, które pobiera maile wszystkich klientów
        debtors = session.query(Debtor.e_mail).all()

        # Pobranie adresów email jako łańcuchy znaków
        emails = [email[0] for email in debtors]
    except Exception as e:
        print("Wystąpił błąd:", e)
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
        print(f"Błąd podczas odczytu pliku: {e}")
        return None



def main():
    # Dane do wysyłania emaila
    current_folder = os.path.dirname(os.path.abspath(__file__))
    sender_email = "#######"  # Mail konta Zoho

    subject = "Prośba o uregulowanie płatności !!!!!!!"
    file_path = os.path.join(current_folder, "prośba.docx")
    body = read_message_from_file(file_path)

    if body:
        # Pobranie hasła z konsoli (jeśli nie jest już znane)
        password = get_hidden_password("Podaj hasło: ")

        # Wywołanie funkcji pobierającej maile klientów z bazy danych
        emails = get_all_emails()

        # Wyświetlenie wyników
        if emails:
            print("Maile klientów:")
            for email in emails:
                print(email)
        else:
            print("Nie udało się pobrać danych z bazy.")

        # Wywołanie funkcji wysyłającej email dla każdego adresu email z listy
        for recipient_email in emails:
            send_email(sender_email, password, recipient_email, subject, body)

        # Usuwanie pliku 'debtors.db' po wysłaniu wiadomości e-mail dla wszystkich adresów
        try:
            os.remove('debtors.db')
            print("Plik 'debtors.db' został usunięty po wysłaniu wiadomości e-mail dla wszystkich adresów.")
        except Exception as e:
            print(f"Błąd podczas usuwania pliku 'debtors.db' po wysłaniu wiadomości e-mail dla wszystkich adresów: {e}")

