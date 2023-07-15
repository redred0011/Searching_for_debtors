import csv

def find_account_number_in_csv(account_number, filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if account_number in row:
                amount = row[-3]
                currency = row[-1]
                print(f"Kwota: {amount} {currency}")

# Example usage
account_to_find = '68 1050 1230 1000 0090 3037 2263'  #numer konta który jest dłużnikiem 
csv_file = 'bank_statements.csv' #nazwa pliku CSV 
find_account_number_in_csv(account_to_find, csv_file)

