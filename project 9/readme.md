# 💰 Expense Tracker

A simple command-line **Expense Tracker** built using Python.
It allows users to record, view, search, summarize, and delete their daily expenses.

The project stores all expense data in a CSV file, so the data remains available even after the program is closed.

---

## 🚀 Features

* ➕ Add new expenses
* 📋 View all expenses
* 💰 Calculate total expenses
* 📊 View category-wise expense summary
* 🔍 Search expenses by category
* 📅 Search expenses by date
* 🗑️ Delete expenses
* 💾 Automatically save data to a CSV file
* 📆 Enter a custom date or use today's date
* 🏷️ Multiple expense categories
* 🧑‍💻 Beginner-friendly command-line interface

---

## 🛠️ Technologies Used

* Python 3
* CSV
* DateTime
* OS

No external Python packages are required.

---

## 📁 Project Structure

```text
expense-tracker/
│
├── expense_tracker.py
├── expenses.csv
├── README.md
└── requirements.txt
```

### Files

| File                 | Description                |
| -------------------- | -------------------------- |
| `expense_tracker.py` | Main Python program        |
| `expenses.csv`       | Stores expense information |
| `README.md`          | Project documentation      |
| `requirements.txt`   | Python dependencies        |

---

## 📋 Expense Categories

The application supports the following categories:

1. Food
2. Transport
3. Shopping
4. Bills
5. Education
6. Entertainment
7. Health
8. Other

---

## ⚙️ Requirements

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project directory

```bash
cd expense-tracker
```

### 3. Run the program

```bash
python expense_tracker.py
```

The `expenses.csv` file will automatically be created when the program starts if it does not already exist.

---

## 🖥️ Main Menu

```text
========================================
          EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Total Expenses
4. Category Summary
5. Search Expenses
6. Delete Expense
7. Exit
========================================
```

---

## ➕ Adding an Expense

Select:

```text
1. Add Expense
```

Example:

```text
Enter amount (₹): 250

Categories:
1. Food
2. Transport
3. Shopping
4. Bills
5. Education
6. Entertainment
7. Health
8. Other

Choose category: 1
Enter description: Lunch
Enter date (YYYY-MM-DD) or press Enter for today:
```

The expense is saved automatically.

---

## 📋 Viewing Expenses

Select:

```text
2. View Expenses
```

Example:

```text
ID   Date         Category         Description                    Amount
------------------------------------------------------------------------
1    2026-09-15   Food             Lunch                         ₹250.00
2    2026-09-15   Transport        Bus ticket                    ₹50.00
3    2026-09-14   Education        Books                        ₹500.00
```

---

## 💰 Total Expenses

Select:

```text
3. Total Expenses
```

Example:

```text
========== TOTAL EXPENSES ==========
Total money spent: ₹800.00
```

---

## 📊 Category Summary

Select:

```text
4. Category Summary
```

Example:

```text
========== CATEGORY SUMMARY ==========
Education            ₹500.00
Food                 ₹250.00
Transport             ₹50.00
--------------------------------
Total                ₹800.00
```

This helps identify where most of your money is being spent.

---

## 🔍 Search Expenses

You can search expenses by:

* Category
* Date

Example:

```text
1. Search by Category
2. Search by Date

Enter your choice: 1
Enter category: Food
```

The program displays all matching expenses.

---

## 🗑️ Delete Expense

Select:

```text
6. Delete Expense
```

Enter the ID of the expense you want to remove.

Example:

```text
Enter expense ID to delete: 2

Expense found:
Date: 2026-09-15
Category: Transport
Description: Bus ticket
Amount: ₹50.00

Are you sure you want to delete it? (y/n): y

Expense deleted successfully!
```

---

## 💾 Data Storage

Expenses are stored in:

```text
expenses.csv
```

The CSV file has the following columns:

```text
ID
Date
Category
Description
Amount
```

Example:

```csv
ID,Date,Category,Description,Amount
1,2026-09-15,Food,Lunch,250.00
2,2026-09-15,Transport,Bus ticket,50.00
3,2026-09-14,Education,Books,500.00
```

---

## 🧠 Concepts Practiced

This project is useful for learning:

* Variables
* Data types
* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Exception handling
* File handling
* CSV files
* Date and time
* Searching
* Data aggregation
* Basic CRUD operations

CRUD means:

* **C** — Create
* **R** — Read
* **U** — Update
* **D** — Delete

---

## 🔮 Future Improvements

Possible upgrades include:

* 📈 Expense charts and graphs
* 📅 Monthly expense reports
* 💵 Monthly budget limits
* ⚠️ Budget warning notifications
* ✏️ Edit/update existing expenses
* 📊 Export reports to Excel
* 🔐 User login
* 🗄️ SQLite database
* 🖥️ GUI using Tkinter
* 🌐 Web version using Flask
* 📱 Mobile-friendly version

---

## 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/your-username`

---

## 📄 License

This project is open-source and available for educational purposes.
