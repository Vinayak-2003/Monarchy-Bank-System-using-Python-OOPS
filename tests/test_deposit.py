import pytest
from unittest.mock import patch
# from utilities.deposit import deposit_amount_func
# from ..utilities.deposit import deposit_amount_func

customer_ID = 101
amount = 1000
BANK_INTEREST = 2
LOAN_INTEREST = 2

# @pytest.fixture
# def mock_dbops(mocker):
#     return mocker.patch("database_ops.DatabaseOps")


@patch("database_ops.DatabaseOps")
def test_deposit_amount_func_with_loan(dbops_instance):
    
    # mock_fetch_data = mock_dbops.fetch_data("account", customer_ID, "Amount")
    
    data = dbops_instance.deposit_amount_func(customer_ID, amount)
    
    bank_amount = BANK_INTEREST*amount*0.01
    bank_profit = 100000 + bank_amount
    assert bank_profit == 100020
    loan_amount = LOAN_INTEREST*0.01*amount
    assert loan_amount == 20
    expected_customer_balance = 5000 + amount - bank_amount - loan_amount
    assert expected_customer_balance == 5960
    expected_loan_remaining = 3000 - loan_amount
    assert expected_loan_remaining == 2980
    
@patch("database_ops.DatabaseOps")
def test_deposit_amount_func_without_loan(dbops_instance):
    
    data = dbops_instance.deposit_amount_func(customer_ID, amount)
    
    bank_amount = BANK_INTEREST*amount*0.01
    bank_profit = 100000 + bank_amount
    assert bank_profit == 100020
    expected_customer_balance = 5000 + amount - bank_amount
    assert expected_customer_balance == 5980
    
