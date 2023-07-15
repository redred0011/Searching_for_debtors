import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import docx

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

# Dane do wysyłania emaila
current_folder = os.path.dirname(os.path.abspath(__file__))
sender_email = 'XXXXXXX' # Mail konta Zoho
sender_password = 'XXXXXX'  # hasło konta Zoho
# Wprowadzanie adresu e-mail odbiorcy
recipient_email = input("Podaj adres e-mail odbiorcy: ")
subject = "Prośba o uregulowanie płatności"

# Wczytywanie treści wiadomości z pliku "prośba.docx"
file_path = os.path.join(current_folder, "prośba.docx")

# Obsługa pliku DOCX za pomocą biblioteki python-docx
doc = docx.Document(file_path)
body = '\n'.join([para.text for para in doc.paragraphs])

print("Treść wiadomości z pliku:")
print(body)

# Wywołanie funkcji send_email do wysłania wiadomości
send_email(sender_email, sender_password, recipient_email, subject, body)

