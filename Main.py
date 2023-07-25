
from search_number_account import main as search_number_account_main
from database import main as database_main
from sending_mail import main as sending_mail_main
from sending_whats_app import main as sending_whats_app_main

def main_function():
    print("--------------------------------")
    print("Searching for indebted companies")
    choose = input("Send reminder by email - M? / WhatsApp - W?:").lower()
    
    if choose == "m":
        
        choose_options = input("Database changes - Z / Search for debtor - S: ").lower()
        
        if choose_options == 'z':
            database_main()
        
        elif choose_options == 's':
            search_number_account_main()
            
            send = input("Do you want to send a message? Yes - T / No - N:").lower()
            
            if send == 't':
                sending_mail_main()
                
            elif send == 'n':
                main_function()
            else:
                main_function()

    elif choose == "w":
        
        choose_options = input("Database changes - Z / Search for debtor - S: ").lower()
        
        if choose_options == 'z':
            database_main()
            
        elif choose_options == 's':
            search_number_account_main()
            
            send = input("Do you want to send a message? Yes - T / No - N: ").lower()
            
            if send == 't':
                sending_whats_app_main()
                
            elif send == 'n':
                main_function()
            else:
                main_function()

    main_function()

main_function()
