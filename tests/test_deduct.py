import pytest
from unittest.mock import patch, MagicMock
# from utilities.deduct import deduct_amount_func

customer_ID = 101
amount = 1000
BANK_INTEREST = 2
LOAN_INTEREST = 2

@patch("database_ops.DatabaseOps.fetch_data")
def test_deduct_amount_with_loan(dbops_instance):
    
    customer_balance = dbops_instance.fetch_data("account", customer_ID, "Amount")
    
    bank_interest_amount = BANK_INTEREST*0.01*amount
    bank_amount = 100000 + bank_interest_amount
    assert bank_amount == 100020
    loan_interest_amount = LOAN_INTEREST*0.01*amount
    assert loan_interest_amount == 20
    new_balance_amount = 5000 - amount - bank_interest_amount - loan_interest_amount
    assert new_balance_amount == 3960
    
@patch("database_ops.DatabaseOps")
def test_deduct_amount_without_loan(dbops_instance):
    
    customer_balance = dbops_instance.fetch_data("account", customer_ID, "Amount")
    
    bank_interest_amount = BANK_INTEREST*0.01*amount
    bank_amount = 100000 + bank_interest_amount
    assert bank_amount == 100020
    new_balance_amount = 5000 - amount - bank_interest_amount
    assert new_balance_amount == 3980