import sending_mail
import search_number_account


def main():

    print("--------------------------------")
    print("Szukanie firm które są zadłużone")
    choose = input("Wysyłanie przypomnienia mailem - M?/What's app'em - W?:").lower()
    
    if choose == "m":
        