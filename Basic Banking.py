# Student Name: Arjun Bindhu Suresh
# Student ID: 100990351
# Date: 2024-11-15

import json
import os
from datetime import datetime

# File to store account data
ACCOUNT_DATA_FILE = "accounts_data.json"

# Load existing account data from the file
def load_accounts():
    if os.path.exists(ACCOUNT_DATA_FILE):
        with open(ACCOUNT_DATA_FILE, 'r') as file:
            return json.load(file)
    return []  

# Save account data to the file
def save_accounts(accounts):
    with open(ACCOUNT_DATA_FILE, 'w') as file:
        json.dump(accounts, file, indent=4)

# Function to create a new account
def create_account(accounts):
    # Taking user input for account details
    account_number = input("Enter Account Number: ")
    name = input("Enter Account Holder's Name: ")
    initial_balance = float(input("Enter Initial Deposit Amount: "))

    # Get today's date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Creating a new account as a dictionary
    account = {
        'Account Number': account_number,
        'Name': name,
        'Balance': initial_balance,
        'Date Created': current_date
    }

    # Adding the new account to the accounts list
    accounts.append(account)

    # Save updated list of accounts to the file
    save_accounts(accounts)

    print(f"Account for {name} with Account Number {account_number} has been created successfully!")

# Function to deposit money into an account
def deposit_money(accounts):
    account_number = input("Enter Account Number to deposit into: ")

    # Find the account by account number
    for account in accounts:
        if account['Account Number'] == account_number:
            deposit_amount = float(input(f"Enter amount to deposit to account {account_number}: "))
            account['Balance'] += deposit_amount
            save_accounts(accounts)
            print(f"Deposit successful! New Balance: {account['Balance']}")
            return
    
    print("Account not found.")

# Function to withdraw money from an account
def withdraw_money(accounts):
    account_number = input("Enter Account Number to withdraw from: ")

    # Find the account by account number
    for account in accounts:
        if account['Account Number'] == account_number:
            withdrawal_amount = float(input(f"Enter amount to withdraw from account {account_number}: "))
            if withdrawal_amount <= account['Balance']:
                account['Balance'] -= withdrawal_amount
                save_accounts(accounts)
                print(f"Withdrawal successful! New Balance: {account['Balance']}")
            else:
                print("Insufficient balance.")
            return
    
    print("Account not found.")

# Function to check the balance of an account
def check_balance(accounts):
    account_number = input("Enter Account Number to check balance: ")

    # Find the account by account number
    for account in accounts:
        if account['Account Number'] == account_number:
            print(f"Account Balance for Account Number {account_number}: {account['Balance']}")
            return
    
    print("Account not found.")

# Main function 
def main():
    accounts = load_accounts()  
    
    while True:
        print("\nBasic Banking System")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        # Taking user choice 
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit_money(accounts)
        elif choice == '3':
            withdraw_money(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
