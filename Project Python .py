#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class User:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.accounts = []

    def register(self):
        # You can add registration logic here, like storing user details in a database
        print(f"User {self.username} registered successfully!")

    def login(self, entered_password):
        if entered_password == self.password:
            print(f"Welcome, {self.username}! You're logged in.")
        else:
            print("Invalid password. Please try again.")

    def update_profile(self, new_username=None, new_password=None, new_email=None):
        if new_username:
            self.username = new_username
        if new_password:
            self.password = new_password
        if new_email:
            self.email = new_email
        print("Profile updated successfully!")


# In[ ]:


# Creating a User instance
new_user = User(user_id=1, username="shimaa", password="sho1232001", email="shimaaabdelaal102@gmail.com")
new_user.register()
entered_password = input("Enter your password to log in: ")
new_user.login(entered_password)


# In[ ]:


class Customer(User):
    def __init__(self, user_id, username, password, email):
        super().__init__(user_id, username, password, email)
        self.account_balances = {}  # Account balances stored as a dictionary
        self.transaction_history = {}


    def view_account_balance(self, account_type):
        if account_type in self.account_balances:
            print(f"Account balance for {account_type}: {self.account_balances[account_type]}")
        else:
            print(f"You don't have a {account_type} account.")

    def view_transaction_history(self, account_type):
        if account_type in self.transaction_history:
            print(f"Transaction history for {account_type}:")
            for transaction in self.transaction_history[account_type]:
                print(transaction)
        else:
            print(f"No transaction history found for {account_type} account.")

    def transfer_money(self, from_account, to_account, amount):
        if from_account in self.account_balances and to_account in self.account_balances:
            if self.account_balances[from_account] >= amount:
                self.account_balances[from_account] -= amount
                self.account_balances[to_account] += amount
                # Record transaction history
                self._record_transaction(from_account, f"Transferred {amount} to {to_account}")
                self._record_transaction(to_account, f"Received {amount} from {from_account}")
                print(f"{amount} successfully transferred from {from_account} to {to_account}.")
            else:
                print("Insufficient balance for the transfer.")
        else:
            print("One or both accounts do not exist.")

    def deposit_money(self, account_type, amount):
        if account_type in self.account_balances:
            self.account_balances[account_type] += amount
            # Record transaction history
            self._record_transaction(account_type, f"Deposited {amount}")
            print(f"{amount} successfully deposited to {account_type}.")
        else:
            print(f"You don't have a {account_type} account.")

    def withdraw_money(self, account_type, amount):
        if account_type in self.account_balances:
            if self.account_balances[account_type] >= amount:
                self.account_balances[account_type] -= amount
                # Record transaction history
                self._record_transaction(account_type, f"Withdrew {amount}")
                print(f"{amount} successfully withdrawn from {account_type}.")
            else:
                print("Insufficient balance for the withdrawal.")
        else:
            print(f"You don't have a {account_type} account.")

    def _record_transaction(self, account_type, transaction):
        if account_type in self.transaction_history:
            self.transaction_history[account_type].append(transaction)
        else:
            self.transaction_history[account_type] = [transaction]



# In[ ]:


# Creating a customer instance
customer = Customer(user_id=1, username="esraa", password="123456", email="esraa123@.com")
# Adding account balances for the customer
customer.account_balances = {'saving': 1000, 'checking': 500}

# Viewing account balance and transaction history
customer.view_account_balance('saving')
customer.view_transaction_history('checking')

print()

# Transferring money between accounts
customer.transfer_money('saving', 'checking', 200)
# Depositing and withdrawing money
customer.deposit_money('saving', 300)
customer.withdraw_money('checking', 100)


# In[ ]:


class BankStaff(User):
    def __init__(self, user_id, username, password, email, staff_id, role):
        super().__init__(user_id, username, password, email)
        self.staff_id = staff_id
        self.role = role

    def approve_account_creation(self, user, account_type):
        user.accounts.append(account_type)
        print(f"Account creation for {user.username} approved. {account_type} account created.")

    def freeze_account(self, user, account_type):
        if account_type in user.accounts:
            print(f"{account_type} account for {user.username} has been frozen.")
        else:
            print(f"{user.username} doesn't have a {account_type} account.")

    def unfreeze_account(self, user, account_type):
        if account_type in user.accounts:
            print(f"{account_type} account for {user.username} has been unfrozen.")
        else:
            print(f"{user.username} doesn't have a {account_type} account.")

    def view_customer_information(self, user):
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Accounts: {', '.join(user.accounts)}")


# In[ ]:


# Creating a bank staff instance
bank_staff = BankStaff(
    user_id=2,
    username="Shimaa",
    password="shimaa1232001",
    email="shimaa123@gmail.com",
    staff_id="sh123",
    role="Manager"
)

# Creating a user
new_user = User(user_id=1, username="sara", password="sara123", email="sara23@gmail.com")
user2= User(user_id=2, username="Rahma", password="Rahma123", email="rahma123@gmail.com")

print()

# Approving account creation for the user by the bank staff
bank_staff.approve_account_creation(new_user, "saving")
bank_staff.approve_account_creation(user2, "checking")

print()

# Freezing and unfreezing accounts by bank staff
bank_staff.freeze_account(new_user, "saving")
bank_staff.unfreeze_account(new_user, "saving")
bank_staff.unfreeze_account(user2, "checking")

print()

# Viewing customer information by bank staff
bank_staff.view_customer_information(new_user)
bank_staff.view_customer_information(user2)


# In[ ]:


class Account:

# Attributes: Account number, account type (e.g., savings, checking), balance, owner (an instance of the Customer class).
    def __init__(self, account_num, account_type, balance, owner):
        self.account_num = account_num
        self.account_type = account_type
        self.balance = balance 
        self.owner = owner
        self.is_frozen = False


# Methods: Display account information, update account balance.
    def display_account_info(self):
        print(f"Account Number : {self.account_num}")
        print(f"Account Type : {self.account_type}")
        print(f"Balance : {self.balance}")
        print(f"Owner : {self.owner.username}")  # an instance of the Customer class 
        # By passing customer as the value for the owner attribute during the creation of the Account object he will take the username as its owner 

    def update_account_balance(self, amount, transaction_type):
        # Check the status of the account:
        if not self.is_frozen:
            if transaction_type == "deposit":
                self.balance += amount
                print(f"Hi {self.owner.username}, your account Number {self.account_num} balance is updated to: {self.balance}")
                
            elif transaction_type == "withdrawal":
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Hi {self.owner.username}, your account Number {self.account_num} Withdrawal of {amount} and their balance is updated to: {self.balance}")
                else:
                    print(f"Sorry {self.owner.username}, Not Enough Money")
            else:
                print("please choose deposit or withdrawal only ")
        else:
            print(f"Sorry {self.owner.username}, but your Account {self.account_num} is frozen")


# In[ ]:


# Creating a Customer
customer_1 = Customer(user_id=4, username="Rahma", password="987", email="rahmatareq@try.com")

# Creating an Account
account_1 = Account(account_num="14", account_type="Savings", balance=5000, owner=customer_1)

# Display account information
account_1.display_account_info()

print()

# Perform a deposit
account_1.update_account_balance(amount=1500, transaction_type="deposit")

# Display updated account information
account_1.display_account_info()

print()


# Perform a withdrawal
withdrawal_amount = 2000
account_1.update_account_balance(amount=withdrawal_amount, transaction_type="withdrawal")
# Display updated account information
account_1.display_account_info()

print()

# Set the account to be frozen
account_1.is_frozen = True


# Try to perform a deposit on a frozen account
account_1.update_account_balance(amount=1500, transaction_type="deposit")
account_1.display_account_info()


# In[ ]:


from datetime import datetime
class Transaction:

    def __init__(self, transaction_id, amount, transaction_type, sender, receiver = None):
        self.transaction_id = transaction_id
        self.timestamp = datetime.now()
        self.sender = sender.username
        self.receiver = receiver.username if receiver is not None else ""
        self.amount = amount
        self.transaction_type = transaction_type

    recorded_transactions = {}  # Class attribute to store all transactions

    def record_transaction(self):
        transaction_details = {
            "Transaction ID": self.transaction_id,
            "Timestamp": self.timestamp,
            "Sender": self.sender,
            "Receiver": self.receiver,
            "Amount": self.amount,
            "Transaction Type": self.transaction_type
        }
        self.recorded_transactions[self.transaction_id] = transaction_details

        print("Transaction recorded successfully!")

    def view_transaction_details(self):
        if self.transaction_id not in self.recorded_transactions:
            print("Transaction not found")
            return

        transaction_details = self.recorded_transactions[self.transaction_id]
        print("Transaction Details:")
        print(f"Transaction ID: {transaction_details['Transaction ID']}")
        print(f"Timestamp: {transaction_details['Timestamp']}")
        print(f"Sender: {transaction_details['Sender']}")
        print(f"Receiver: {transaction_details['Receiver']}")
        print(f"Amount: {transaction_details['Amount']}")
        print(f"Transaction Type: {transaction_details['Transaction Type']}")


# In[ ]:


customer = Customer(user_id=1, username="rahma", password="123456", email="rahma123@gmail.com")
customer2 = Customer(user_id=2, username="marwa", password="marwa123", email="marwa123@gmail.com")

transaction = Transaction(
    transaction_id="12345",
    sender=customer,
    receiver=customer2,
    amount=100,
    transaction_type="transfer"
)

customer3 = Customer(user_id=3, username="esraa", password="5682", email="esraa123@gmail.com")
transaction2 = Transaction(
    transaction_id="9999",
    sender=customer3,
    amount=500,
    transaction_type="deposite"
)

# Recording the transaction
transaction.record_transaction()
transaction2.record_transaction()
# Viewing transaction details
transaction.view_transaction_details()
transaction2.view_transaction_details()

