import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
sender_email = '#####' # Mail konta Zoho
sender_password = '#####'  # hasło konta Zoho
recipient_email = input("Podaj adres e-mail odbiorcy: ")
subject = input("Podaj temat wiadomości: ")
body = input("Podaj treść wiadomości: ")

# Wywołanie funkcji do wysłania wiadomości email
send_email(sender_email, sender_password, recipient_email, subject, body)

