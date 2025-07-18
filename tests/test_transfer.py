import pytest
from unittest.mock import patch

sender_interest = 4
receiver_interest = 2
customer_ID = 101
amount = 1000
BANK_INTEREST = 2
LOAN_INTEREST = 2
sender_balance = 4000
receiver_balanace = 4000

@patch("database_ops.DatabaseOps")
def test_transfer_func_with_loan(dbops_instance):
    data = dbops_instance.deposit_amount_func(customer_ID, amount)
    
    sending_interest = sender_interest*0.01*amount
    interest_sending_amount = amount + sending_interest
    assert interest_sending_amount == 1040
    receiving_interest = receiver_interest*0.01*amount
    interest_receiving_amount = amount + receiving_interest
    assert interest_receiving_amount == 1020
    bank_profit = 100000 + (interest_sending_amount - interest_receiving_amount)
    assert bank_profit == 100020
    
    loan_interest_amount = LOAN_INTEREST*amount*0.01
    sender_New_balance = sender_balance - interest_sending_amount - loan_interest_amount
    assert sender_New_balance == 2940
    receiver_new_balanace = receiver_balanace + interest_receiving_amount
    assert receiver_new_balanace == 5020
    

@patch("database_ops.DatabaseOps")
def test_transfer_func_without_loan(dbops_instance):
    data = dbops_instance.deposit_amount_func(customer_ID, amount)
    
    sending_interest = sender_interest*0.01*amount
    interest_sending_amount = amount + sending_interest
    assert interest_sending_amount == 1040
    receiving_interest = receiver_interest*0.01*amount
    interest_receiving_amount = amount + receiving_interest
    assert interest_receiving_amount == 1020
    bank_profit = 100000 + (interest_sending_amount - interest_receiving_amount)
    assert bank_profit == 100020
    
    sender_New_balance = sender_balance - interest_sending_amount
    assert sender_New_balance == 2960
    receiver_new_balanace = receiver_balanace + interest_receiving_amount
    assert receiver_new_balanace == 5020
    

