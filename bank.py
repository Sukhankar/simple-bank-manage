class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            return "Account already exists."
        else:
            self.accounts[account_number] = initial_balance
            return f"Account created successfully with account number {account_number} and initial balance {initial_balance}"

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            return f"Deposited {amount} into account {account_number}. Current balance: {self.accounts[account_number]}"
        else:
            return "Account does not exist."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                return f"Withdrew {amount} from account {account_number}. Current balance: {self.accounts[account_number]}"
            else:
                return "Insufficient balance."
        else:
            return "Account does not exist."

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return f"Balance in account {account_number}: {self.accounts[account_number]}"
        else:
            return "Account does not exist."


bank = Bank()


while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        print(bank.create_account(account_number, initial_balance))
    elif choice == '2':
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        print(bank.deposit(account_number, amount))
    elif choice == '3':
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        print(bank.withdraw(account_number, amount))
    elif choice == '4':
        account_number = input("Enter account number: ")
        print(bank.check_balance(account_number))
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")
