from database_ops import DatabaseOps
from constants import BANK_INTEREST, BANK_ID, LOAN_INTEREST

def deduct_amount_func(customer_ID, amount):
    customer_current_balanace = DatabaseOps.fetch_data("account", customer_ID, "Amount")
    bank_balance = DatabaseOps.fetch_data("account", BANK_ID, "Amount")
    isLoan = DatabaseOps.fetch_data("account", customer_ID, "Home_loan")
    
    if customer_current_balanace is None or isLoan is None:
        print(f"Customer_ID {customer_ID} is wrong")
        return
    
    if customer_current_balanace < amount:
        print(f"Customer with Customer-ID {customer_ID} does not have sufficient amount")
    else:
        bank_profit = bank_balance + BANK_INTEREST*0.01*amount
        if isLoan == 1:
            loan_remaining_amount = DatabaseOps.fetch_data("homeloan", customer_ID, "RemainingAmount")
            loan_amount = LOAN_INTEREST*0.01*amount
            new_balance = customer_current_balanace - amount - BANK_INTEREST*0.01*amount - loan_amount
            updated_remaining_amount = loan_remaining_amount - loan_amount
            DatabaseOps.update_account_balance("account", customer_ID, new_balance)
            DatabaseOps.update_account_balance("homeloan", customer_ID, updated_remaining_amount)
        else:
            new_balance = customer_current_balanace - amount - BANK_INTEREST*0.01*amount
            DatabaseOps.update_account_balance("account", customer_ID, new_balance)
        DatabaseOps.update_account_balance("account", BANK_ID, bank_profit)
        print(f"Deducted Amount Rs.{amount} for Customer-ID {customer_ID}")