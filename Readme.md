# _Searching for debtors_

### Main functions program:
- Adding, deleting and changing contractors' data
- Reading bank statement from CSV file named "bank_statements.csv"
- Comparing statement data with data from databases.
- Creating a database of debtors who are not in the bank statement
- Sending payment reminders via mail or what's appa

### Database 

    This code provides a simple customer database management system using 
    SQLAlchemy. It allows users to interact with a SQLite database to 
    perform CRUD (Create, Read, Update, Delete) operations on customer records.
    When running the program, the database interactions will be printed in the
    console (echo=True). If you prefer to hide these logs, you can set echo=False 
    in the create_engine() call.The program is designed to handle user inputs
    gracefully and gives appropriate feedback for incorrect inputs or non-existent
    customer IDs.
    Example Usage
    To add a new customer, run the program and type d at the prompt. Then follow the
    instructions to provide customer details.
    To delete a customer, run the program and type at the prompt. Then follow the instructions
    to provide the ID of the customer you want to delete.
    To update customer information, run the program and type z at the prompt.
    Then follow the instructions to provide the ID of the customer you want to update
    and choose which field to update.
    Feel free to contribute to this project by submitting bug reports, feature requests,
    or pull requests on the GitHub repository.


### Database_Debtors
   
    Welcome to the Debtors database! This is a simple Python application that utilizes 
    SQLAlchemy to create and manage a database for keeping track of debtors. Whether you
    are an individual, a small business, or an organization, this application will help 
    you organize and store debtor information efficiently.

### Search_numer_account

    This python script manages two databases: one for customers and one for debtors. 
    It uses the SQLAlchemy library for effective interaction with databases. 
    This function searches for bank numbers in the database and compares them to 
    account numbers on the bank statement, if such a number is not on the statement, 
    the data is redirected to the debtors database

### Sending_mail

    This function is used to send a notification about debt by e-mail from
    ZOHO e-mail (it is possible to adapt the code to each e-mail). The code
    retrieves data from the debtors database, then sends messages after entering 
    the login password.

### Sending_whats_app

    This function is used to send a Whatsapp debt notification to indebted
    users, data is downloaded from the debtors database and a message from
    the program file
### Main 
    This program function is the main handler function. it combines the 
    entire code in its entirety and allows you to meet expectations, 
    i.e. search for debtors
## Things used

- [Visual Studio Code] - Helps me with the code I entered
- [Git Bash] - Helps me connect online and standard repository
- [Github] - My main repositories
- [Sqlalchemy] - Data storage
- [Getpass] - Password hiding
- [pywhatkit] - Sending whatsapp messages
- [mail.mime.multipart] - Sending mail messages

## License 

_redred00_   


