# Assuming the module sending_mail is correctly named send_mail (adjust accordingly if it's different)
import sending_mail
from search_number_account import main as search_number_account_main
from database import main as database_main
from sending_mail import main as sending_mail_main

def main_function():
    print("--------------------------------")
    print("Szukanie firm które są zadłużone")
    choose = input("Wysyłanie przypomnienia mailem - M?/What's app'em - W?:").lower()
    
    if choose == "m":
        choose_options = input("Zmiany bazy - Z / Szukanie dłużnika - S: ").lower()
        
        if choose_options == 'z':
            
            database_main()
        
        elif choose_options == 's':
            search_number_account_main()
            
            send  = input("Chcesz wysłać wiadomość? Tak - T / Nie - N:").lower()
            
            if send == 't':
                sending_mail_main()
                
            elif send == 'n':
                main_function()
            else:
                send

    elif choose == "w":
        a = input(":")
       
        
    main_function()

main_function()
