from database_ops import DatabaseOps
from constants import HOMELOAN_COLUMN, MAX_HOME_LOAN_AMOUNT
import uuid

def home_loan_func(customer_ID, loan_amount: int):
    isLoan = DatabaseOps.fetch_data("account", customer_ID, "Home_loan")
    if isLoan == 1:
        print("ALREADY LOAN GRANTED")
    elif loan_amount <= MAX_HOME_LOAN_AMOUNT:
        loan_id = f"MONHMLN-{str(uuid.uuid4().int)[:8]}"
        DatabaseOps.insert_homeloan_data(loan_id, customer_ID, loan_amount, loan_amount)
        DatabaseOps.update_constant_data(customer_ID, HOMELOAN_COLUMN, 1)
        print("LOAN GRANTED")
    else:
        print("LOAN NOT GRANTED")