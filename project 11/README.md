# 🏧 ATM Simulation

A beginner-friendly **console-based ATM Simulation** built with Python.

This project simulates common ATM operations such as PIN authentication, checking balance, depositing money, withdrawing money, changing the PIN, and viewing transaction history.

Account data is stored locally in a JSON file, so changes remain available after the program is closed and restarted.

---

## ✨ Features

- 🔐 4-digit PIN authentication
- 🔢 Maximum of 3 login attempts
- 💰 Check account balance
- 💵 Deposit money
- 💸 Withdraw money
- 🚫 Prevent withdrawals when balance is insufficient
- 🔑 Change PIN
- 📜 View transaction history
- 💾 Save account data using JSON
- ❌ Input validation
- 🚪 Exit/logout option

---

## 📁 Project Structure

```text
ATM-Simulation/
│
├── atm_simulation.py
├── account.json
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

- Python 3
- JSON
- Python Standard Library
- `datetime`
- `pathlib`

No external Python packages are required.

---

## ⚙️ Requirements

Install **Python 3.8 or later**.

Check your Python version:

```bash
python --version
```

or:

```bash
py --version
```

---

## 🚀 How to Run

### 1. Clone or download the project

Open your terminal in the project directory.

### 2. Run the program

```bash
python atm_simulation.py
```

On Windows, you can also use:

```bash
py atm_simulation.py
```

---

## 🔐 Sample Login

The sample `account.json` contains:

```text
PIN: 1234
```

After successful authentication, the ATM menu appears.

> **Note:** `1234` is only a demonstration PIN. Do not use it for a real financial application.

---

## 🖥️ Example

```text
========================================
       WELCOME TO ATM SIMULATION
========================================
Enter your 4-digit PIN: 1234

Welcome, Kailash!

========================================
           ATM SIMULATION
========================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Transaction History
6. Exit
========================================
Enter your choice (1-6):
```

---

## 💰 Check Balance

Select:

```text
1
```

Example:

```text
Current balance: ₹5000.00
```

---

## 💵 Deposit Money

Select:

```text
2
```

Example:

```text
Enter deposit amount: ₹2000
₹2000.00 deposited successfully.
New balance: ₹7000.00
```

The transaction is automatically saved to `account.json`.

---

## 💸 Withdraw Money

Select:

```text
3
```

Example:

```text
Enter withdrawal amount: ₹1000
Please collect your cash: ₹1000.00
Remaining balance: ₹6000.00
```

If the requested amount is greater than the available balance:

```text
Insufficient balance.
```

---

## 🔑 Change PIN

Select:

```text
4
```

You must provide:

1. Current PIN
2. New 4-digit PIN
3. New PIN confirmation

Example:

```text
Enter current PIN: 1234
Enter new 4-digit PIN: 5678
Confirm new PIN: 5678
PIN changed successfully.
```

The new PIN is stored in `account.json`.

---

## 📜 Transaction History

Select:

```text
5
```

Example:

```text
=================================================================
                    TRANSACTION HISTORY
=================================================================
1. 2026-09-23 22:00:00 | Deposit      | ₹   2000.00 | Balance: ₹   7000.00
2. 2026-09-23 22:05:00 | Withdrawal   | ₹   1000.00 | Balance: ₹   6000.00
=================================================================
```

---

## 🗃️ JSON Data Storage

The project uses `account.json` to store account information.

Example:

```json
{
    "account_number": "ATM10001",
    "name": "Kailash",
    "pin": "1234",
    "balance": 5000.0,
    "transactions": []
}
```

The program automatically updates the balance, PIN, and transaction history.

---

## 🧠 Python Concepts Practiced

This project helps you practice:

- Variables
- Data types
- `if`, `elif`, and `else`
- `while` loops
- Functions
- Lists
- Dictionaries
- Exception handling
- File handling
- JSON
- Date and time
- Input validation
- Modular program design

---

## 🔄 Program Flow

```text
Start
  │
  ▼
Load account.json
  │
  ▼
Enter PIN
  │
  ├── Incorrect ──► Retry
  │                   │
  │                   └── 3 failures ──► Exit
  │
  ▼
Authentication Successful
  │
  ▼
Display ATM Menu
  │
  ├── Check Balance
  │
  ├── Deposit Money
  │
  ├── Withdraw Money
  │
  ├── Change PIN
  │
  ├── Transaction History
  │
  └── Exit
  │
  ▼
Save changes to account.json
  │
  ▼
Exit
```

---

## 🔒 Important Security Note

This project is designed for **learning purposes only**.

It is **not a real banking/ATM security system**.

For a production banking application, you should not store PINs as plain text in JSON. A real system would require secure authentication, password/PIN hashing, encryption, access control, audit logging, database transactions, rate limiting, and other security controls.

---

## 🚀 Future Improvements

You can extend this project with:

- [ ] Multiple bank accounts
- [ ] Account number login
- [ ] PIN hashing
- [ ] SQLite/MySQL database
- [ ] ATM cash denomination management
- [ ] Mini statement printing
- [ ] Transfer money between accounts
- [ ] Daily withdrawal limits
- [ ] Admin panel
- [ ] GUI using Tkinter
- [ ] REST API using Flask or FastAPI
- [ ] Unit tests using `unittest` or `pytest`

---

## 👨‍💻 Author

**Kailash**

Python Learning Project

---

## 📄 License

This project is created for educational and practice purposes.
