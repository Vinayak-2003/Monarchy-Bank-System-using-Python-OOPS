from database_ops import DatabaseOps
import random
from datetime import datetime

from constants import HOMELOAN_COLUMN
from utilities.transfer import transfer_money_func
from utilities.deposit import deposit_amount_func
from utilities.deduct import deduct_amount_func
from utilities.homeloan import home_loan_func

DatabaseOps.create_table()
DatabaseOps.create_homeloan_table()

class Account:
    
    def __init__(self, name, contact):
        self.customer_ID = f"MONARCHY-{random.randint(10000,99999)}"
        self.name = name
        self.contact = contact
        self.created_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.updated_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # generate customer information
    def generate_information(self, account_type):
        print(f"Welcome {self.name}! Your customerID is {self.customer_ID} and Amount in your Monarchy {account_type} is {self.amount}")
        
    @staticmethod
    def transfer_money(sender_ID, receiver_ID, transfer_amount, sender_interest, receiver_interest, threshold_transaction_cnt):
        transfer_money_func(sender_ID, receiver_ID, transfer_amount, sender_interest, receiver_interest, threshold_transaction_cnt)
        
    @staticmethod    
    def deposit_amount(customer_ID, amount):
        deposit_amount_func(customer_ID, amount)
        
    @staticmethod
    def deduct_amount(customer_ID, amount):
        deduct_amount_func(customer_ID, amount)

    @staticmethod
    def home_loan(customer_ID, loan_amount: int):
        home_loan_func(customer_ID, loan_amount)
        
    
class SavingsAccount(Account):
    sending_interest = 7
    receiving_interest = 5
    threshold_transaction_cnt = 3
    
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.account_type = "Savings Account"
        self.amount = random.randint(1000,9999)
        DatabaseOps.insert_account_data(self.customer_ID, self.name, self.contact, self.amount, self.created_datetime, self.updated_datetime, self.account_type)
        super().generate_information(self.account_type)
        
    @staticmethod
    def transfer_money(sender_ID, receiver_ID, transfer_amount):
        return super(SavingsAccount, SavingsAccount).transfer_money(sender_ID, receiver_ID, transfer_amount, SavingsAccount.sending_interest, SavingsAccount.receiving_interest, SavingsAccount.threshold_transaction_cnt)
       
    @staticmethod
    def deposit_amount(customer_ID, amount):
        return super(SavingsAccount, SavingsAccount).deposit_amount(customer_ID, amount)
    
    @staticmethod
    def deduct_amount(customer_ID, amount):
        return super(SavingsAccount, SavingsAccount).deduct_amount(customer_ID, amount)
    
    @staticmethod
    def home_loan(customer_ID, loan_amount):
        return super(SavingsAccount, SavingsAccount).home_loan(customer_ID, loan_amount)


class CurrentAccount(Account):
    sending_interest = 4
    receiving_interest = 2
    threshold_transaction_cnt = 5
    
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.account_type = "Current Account"
        self.amount = random.randint(10000,99999)
        DatabaseOps.insert_account_data(self.customer_ID, self.name, self.contact, self.amount, self.created_datetime, self.updated_datetime, self.account_type)
        super().generate_information(self.account_type)
    
    @staticmethod
    def transfer_money(sender_ID, receiver_ID, transfer_amount):
        return super(CurrentAccount, CurrentAccount).transfer_money(sender_ID, receiver_ID, transfer_amount, CurrentAccount.sending_interest, CurrentAccount.receiving_interest, CurrentAccount.threshold_transaction_cnt)
    
    @staticmethod
    def deposit_amount(customer_ID, amount):
        return super(CurrentAccount, CurrentAccount).deposit_amount(customer_ID, amount)
    
    @staticmethod
    def deduct_amount(customer_ID, amount):
        return super(CurrentAccount, CurrentAccount).deduct_amount(customer_ID, amount)
    
    @staticmethod
    def home_loan(customer_ID, loan_amount):
        return super(SavingsAccount, SavingsAccount).home_loan(customer_ID, loan_amount)
    
        
# person = SavingsAccount("Monty", "953726373")
# SavingsAccount.home_loan("MONARCHY-71758", 30000)
# person2 = CurrentAccount("Aman", "975373133")
# SavingsAccount.transfer_money("MONARCHY-10819", "MONARCHY-12202", 2000)
# SavingsAccount.deposit_amount("MONARCHY-71758", 2000)
# SavingsAccount.deduct_amount("MONARCHY-22310", 230)

# CurrentAccount.transfer_money("MONARCHY-10819", "MONARCHY-74147", 500)
# CurrentAccount.home_loan("MONARCHY-74147", 20000)
CurrentAccount.transfer_money("MONARCHY-74147", "MONARCHY-71758", 5000)
