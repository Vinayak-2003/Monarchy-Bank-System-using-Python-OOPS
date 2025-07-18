# Monarchy Banking System

## Introduction 
A Python-based Object-Oriented Programming (OOPS) project simulating a monarchy-style banking system. It features:
 - Savings and Current accounts
 - Custom interest mechanics
 - A home loan system


## 📌 Features

- 🏦 **Account Types**  
  - Savings Account (higher interest, stricter limits)  
  - Current Account (lower interest, more flexibility)  

- 💸 **Transaction Mechanics**  
  - Interest is **added to the receiver** and **deducted from the sender**  
  - Interest rate **decreases after a set number of payments**  
  - Balance **added manually does not earn interest**  

- 💰 **Initial Account Balance**  
  - Assigned randomly by the bank (4-digit number) for Savings Account
  - Assigned randomly by the bank (5-digit number) for Current Account

- ➕ **Add Funds**  
  - Maximum allowed: **4-digit number (≤ 9999)**  

- 🏠 **Home Loan Support**  
  - Max loan amount: ₹8,00,000  
  - EMI deducted on **every send and receive transaction**  
  - Interest applied within EMI 

---

## 📂 Project Structure

```bash
monarchy_banking/
│
├── .pytest_cache/              # Pytest cache files
├── coverage_reports/           # Test coverage reports
├── tests/                      # Unit tests directory
│
├── utilities/                  # Modular service logic
│   ├── __init__.py
│   ├── deduct.py               # Handles interest deduction logic
│   ├── deposit.py              # Deposit functionality
│   ├── homeloan.py             # Home loan and EMI logic
│   ├── transfer.py             # Fund transfer + interest application
│
├── venv/                       # Python virtual environment (excluded from Git)
│
├── __init__.py                 # Main package initializer
├── .coverage                   # Coverage result file
├── .coveragerc                 # Coverage configuration
├── .gitignore                  # Git ignored files
├── constants.py                # Global constants (interest rates, limits, etc.)
├── database_ops.py             # Database simulation / logic
├── main.py                     # Main runner script
├── MonarchyBank.db             # Optional SQLite DB (if used)
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies


## 🚀 Getting Started

1. **Clone the repository and navigate into the folder:**

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Ensure Python is installed** locally and added to the system PATH.

3. **Create a virtual environment (recommended):**

    ```bash
    python -m venv <virtual_env_name>
    ```

4. **Activate the virtual environment:**

    - On **Windows**:
      ```bash
      <virtual_env_name>\Scripts\activate
      ```

    - On **macOS/Linux**:
      ```bash
      source <virtual_env_name>/bin/activate
      ```

5. **Install all dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Start from the main entery point as:**

    ```bash
    python main.py
    ```

---