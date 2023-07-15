import csv
from twilio.rest import Client
import os

def check_account_number_in_csv(account_number, filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if account_number in row:
                    return True
    except Exception as e:
        print(f"An error occurred while checking the CSV file: {e}")
    return False

def send_whatsapp_message(account_number):
    account_sid = os.environ.get('AC65390449ede63df6417cd02d14b23d9a')
    auth_token = os.environ.get('c18532937f4dd004cb8493b9944d782c')
    whatsapp_from = 'whatsapp:+48507853201'
    whatsapp_to = 'whatsapp:+48507853201'

    client = Client(account_sid, auth_token)

    message = f'Dziękujemy za terminową płatność dla numeru konta: {account_number}'
    try:
        client.messages.create(body=message, from_=whatsapp_from, to=whatsapp_to)
    except Exception as e:
        print(f"An error occurred while sending the WhatsApp message: {e}")

account_to_check = '93 1030 0019 0109 8502 5021 3931'
csv_file = 'bank_statements.csv'

if check_account_number_in_csv(account_to_check, csv_file):
    print("Dziękujemy za terminową płatność.")
    send_whatsapp_message(account_to_check)
else:
    print("Numer konta nie został znaleziony w pliku.")

