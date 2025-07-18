import sqlite3
from datetime import datetime
from constants import DATABASE_NAME, ACCOUNT_TABLE_NAME, HOMELOAN_TABLE_NAME

table_mapping = {
    "account": ACCOUNT_TABLE_NAME,
    "homeloan": HOMELOAN_TABLE_NAME
}

current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

class DatabaseOps:
    
    def create_table():
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        CREATE_TABLE_QUERY = f"""
                                CREATE TABLE IF NOT EXISTS {ACCOUNT_TABLE_NAME} (
                                CustomerID VARCHAR(20) PRIMARY KEY, 
                                Name VARCHAR(100), 
                                Contact INTEGER, 
                                Amount INTEGER, 
                                Create_timestamp TEXT, 
                                Updated_timestamp TEXT, 
                                Account_type VARCHAR(100),
                                Transaction_count INTEGER,
                                Home_loan BOOLEAN
                            )"""
        cursor.execute(CREATE_TABLE_QUERY)
        conn.commit()
        conn.close()
        
    def create_homeloan_table():
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        CREATE_TABLE_QUERY = f"""
                                CREATE TABLE IF NOT EXISTS {HOMELOAN_TABLE_NAME}(
                                    LoanID VARCHAR(20) PRIMARY KEY,
                                    CustomerID VARCHAR(20),
                                    LoanAmount INTEGER,
                                    RemainingAmount INTEGER,
                                    LoanCreatedTimestamp TEXT, 
                                    LoanLastUpdatedTimestamp TEXT,
                                    FOREIGN KEY (CustomerID) REFERENCES {ACCOUNT_TABLE_NAME}(CustomerID)
                            )"""
        cursor.execute(CREATE_TABLE_QUERY)
        conn.commit()
        conn.close()
        
    def drop_table():
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE {ACCOUNT_TABLE_NAME}")
        conn.commit()
        conn.close()
        
    def fetch_data(table_name, customer_ID, data):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        RETRIEVE_AMOUNT = f"SELECT {data} FROM {table_mapping[f'{table_name}']} WHERE CustomerID = ?"
        cursor.execute(RETRIEVE_AMOUNT, (customer_ID,))
        data = cursor.fetchone()
        conn.close()
        return data[0]
        
    def insert_account_data(customer_ID, name, contact, amount, created_datetime, updated_datetime, account_type, transaction_count=0, homeloan=0):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        INSERT_QUERY = f"INSERT INTO {ACCOUNT_TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(INSERT_QUERY, (customer_ID, name, contact, amount, created_datetime, updated_datetime, account_type, transaction_count, homeloan))
        conn.commit()
        conn.close()
        
    def insert_homeloan_data(loan_ID, customer_ID, loan_amount, remaining_amount):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        INSERT_QUERY = f"INSERT INTO {HOMELOAN_TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(INSERT_QUERY, (loan_ID, customer_ID, loan_amount, remaining_amount, current_datetime, current_datetime))
        conn.commit()
        conn.close()
        
    def update_account_balance(table_name, customer_ID, updated_balance):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        UPDATE_AMOUNT_QUERY = f"UPDATE {table_mapping[f'{table_name}']} SET Amount = ?, Updated_timestamp = ? WHERE CustomerID = ?"
        UPDATE_LOANAMOUNT_QUERY = f"UPDATE {table_mapping[f'{table_name}']} SET RemainingAmount = ?, LoanLastUpdatedTimestamp = ? WHERE CustomerID = ?"
        UPDATE_QUERY = UPDATE_AMOUNT_QUERY if table_name == "account" else UPDATE_LOANAMOUNT_QUERY
        cursor.execute(UPDATE_QUERY, (updated_balance, current_datetime, customer_ID))
        conn.commit()
        conn.close()
        
    def update_constant_data(customer_ID, column_name, updated_value):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        UPDATE_QUERY = f"UPDATE {ACCOUNT_TABLE_NAME} SET {column_name} = ? WHERE CustomerID = ?"
        cursor.execute(UPDATE_QUERY, (updated_value, customer_ID))
        conn.commit()
        conn.close()
        
    def alter_table(table_name, column_name, data_type):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        ALTER_QUERY = f"ALTER TABLE {table_name} ADD {column_name} {data_type}"
        cursor.execute(ALTER_QUERY)
        conn.commit()
        conn.close()
        
    def delete_data(table_name, id):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        DELETE_USER_QUERY = f"DELETE FROM {table_mapping[f'{table_name}']} WHERE CustomerID = ?"
        DELETE_LOAN_QUERY = f"DELETE FROM {table_mapping[f'{table_name}']} WHERE LoanID = ?"
        DELETE_QUERY = DELETE_USER_QUERY if table_name == "account" else DELETE_LOAN_QUERY
        cursor.execute(DELETE_QUERY, (id,))
        conn.commit()
        conn.close()
        
        
        
# DatabaseOps.insert_account_data("MONARCHY-00001", "MONARCHY BANK", "9999999999", 0, datetime.now().strftime("%d-%m-%Y %H:%M:%S"), datetime.now().strftime("%d-%m-%Y %H:%M:%S"), "BANK VAULT")
# DatabaseOps.alter_table("Accounts", "Home_loan", "BOOLEAN")
# DatabaseOps.delete_data("homeloan", "32027920")