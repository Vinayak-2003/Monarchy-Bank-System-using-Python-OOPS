from database_ops import DatabaseOps
from constants import BANK_ID, TRANSACTION_COLUMN, LOAN_INTEREST


def transfer_money_func(sender_ID, receiver_ID, transfer_amount, sender_interest, receiver_interest, threshold_transaction_cnt):
        sender_balance = DatabaseOps.fetch_data("account", sender_ID, "Amount")
        receiver_balance = DatabaseOps.fetch_data("account", receiver_ID, "Amount")
        bank_balance = DatabaseOps.fetch_data("account", BANK_ID, "Amount")
        transaction_balance = DatabaseOps.fetch_data("account", sender_ID, "Transaction_count")
        isLoan = DatabaseOps.fetch_data("account", sender_ID, "Home_loan")
        
        if sender_balance is None or receiver_balance is None or isLoan is None:
            print(f"Either sender ID {sender_ID} or Receiver ID {receiver_ID} is wrong")
            return
        
        if transaction_balance % threshold_transaction_cnt == 0:
            cnt = transaction_balance / threshold_transaction_cnt
            sender_interest -= (cnt*0.01)
            receiver_interest -= (cnt*0.01)
            
        interest_transfer_amount = transfer_amount + (sender_interest*0.01*transfer_amount)
        receiver_receive_amount = transfer_amount + (receiver_interest*0.01*transfer_amount)
        bank_profit = bank_balance + (interest_transfer_amount - receiver_receive_amount)
        
        if interest_transfer_amount <= sender_balance:
            if isLoan == 1:
                loan_remaining_amount = DatabaseOps.fetch_data("homeloan", sender_ID, "RemainingAmount")
                loan_amount = LOAN_INTEREST*transfer_amount*0.01
                sender_balance = sender_balance - interest_transfer_amount - loan_amount
                print("+++++++++++++++++++", sender_balance)
                updated_remaining_amount = loan_remaining_amount - loan_amount
                DatabaseOps.update_account_balance("account", sender_ID, sender_balance)
                DatabaseOps.update_account_balance("homeloan", sender_ID, updated_remaining_amount)
            else:
                sender_balance -= interest_transfer_amount
                DatabaseOps.update_account_balance("account", sender_ID, sender_balance)
                
            receiver_balance += receiver_receive_amount
            DatabaseOps.update_account_balance("account", receiver_ID, receiver_balance)
            DatabaseOps.update_account_balance("account", BANK_ID, bank_profit)
            DatabaseOps.update_constant_data(sender_ID, TRANSACTION_COLUMN, transaction_balance+1)
            print(f"Transfered Amount Rs.{receiver_receive_amount} from Customer-ID {sender_ID} to {receiver_ID}")
        else:
            print("Insufficient Amount !!")