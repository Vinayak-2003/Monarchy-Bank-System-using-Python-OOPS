import sqlite3
from database_ops import DatabaseOps
from constants import DATABASE_NAME, ACCOUNT_TABLE_NAME, HOMELOAN_TABLE_NAME

# def test_create_table(mocker):
#     mock_conn = mocker.patch("sqlite3.connect")
#     mock_cursor = mock_conn.return_value.cursor.return_value
    
#     CREATE_TABLE_QUERY = f"""
                            #     CREATE TABLE IF NOT EXISTS {ACCOUNT_TABLE_NAME} (
                            #     CustomerID VARCHAR(20) PRIMARY KEY, 
                            #     Name VARCHAR(100), 
                            #     Contact INTEGER, 
                            #     Amount INTEGER, 
                            #     Create_timestamp TEXT, 
                            #     Updated_timestamp TEXT, 
                            #     Account_type VARCHAR(100),
                            #     Transaction_count INTEGER,
                            #     Home_loan BOOLEAN
                            # )"""
                            
#     DatabaseOps.create_homeloan_table()
#     mock_conn.assert_called_once_with(DATABASE_NAME)
#     mock_cursor.execute.assert_called_once_with(CREATE_TABLE_QUERY)
    
def test_drop_table(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value
    DatabaseOps.drop_table()
    mock_conn.assert_called_once_with(DATABASE_NAME)
    mock_cursor.execute.assert_called_once_with(f"DROP TABLE Accounts")
    
def test_fetch_data(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value
    RETRIEVE_AMOUNT = f"SELECT Amount FROM {ACCOUNT_TABLE_NAME} WHERE CustomerID = ?"
    DatabaseOps.fetch_data("account", "MONARCHY-101", "Amount")
    mock_conn.assert_called_once_with(DATABASE_NAME)
    mock_cursor.execute.assert_called_once_with(RETRIEVE_AMOUNT, ("MONARCHY-101",))
    
def test_insert_data(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value
    INSERT_QUERY = f"INSERT INTO {ACCOUNT_TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    DatabaseOps.insert_account_data("MONARCHY-101", "test_name", 9999999999, 5000, "19-04-2025 17:29:15", "19-04-2025 17:29:15", "Savings Account", 4, 1)
    mock_conn.assert_called_once_with(DATABASE_NAME)
    mock_cursor.execute.assert_called_once_with(INSERT_QUERY, ("MONARCHY-101", "test_name", 9999999999, 5000, "19-04-2025 17:29:15", "19-04-2025 17:29:15", "Savings Account", 4, 1))
    
def test_