# 💰 Smart Interest Calculator

A beginner-friendly Python project that calculates **Simple Interest** and **Compound Interest** and provides a comparison between them.

The project also includes currency selection, different time units, input validation, repeated calculations, interest breakdown, and calculation history.

---

## 📌 Features

### 🧮 1. Simple Interest

Calculates Simple Interest using:

**SI = (P × R × T) / 100**

Where:

* `P` = Principal amount
* `R` = Rate of interest
* `T` = Time in years

---

### 💹 2. Compound Interest

Calculates Compound Interest using:

**CI = P(1 + R/100)^T - P**

The current version uses **annual compounding**.

---

### 📊 3. SI vs CI Comparison

The calculator compares:

* Simple Interest
* Compound Interest
* Difference between the two
* Which interest is higher

Example:

```text
Simple Interest     : ₹1,000.00
Compound Interest   : ₹1,025.00
Difference          : ₹25.00
Result              : Compound Interest is higher.
```

---

### 📅 4. Multiple Time Units

The user can enter time in:

* Years
* Months
* Days

The program automatically converts months and days into years.

```text
Months → Months / 12
Days   → Days / 365
```

---

### 💰 5. Currency Selection

The calculator supports:

* ₹ INR
* $ USD
* € EUR
* £ GBP

The selected currency symbol is displayed in the calculation results.

---

### 🔄 6. Multiple Calculations

The program uses a menu-driven system, allowing users to perform multiple calculations without restarting the program.

```text
MAIN MENU

1. Calculate Interest
2. View Calculation History
3. Exit
```

---

### ⚠️ 7. Input Validation

The program checks user input and prevents invalid values.

It handles:

* Negative numbers
* Zero values
* Non-numeric input
* Invalid menu choices
* Invalid currency choices
* Invalid time-unit choices

Example:

```text
Enter principal amount: -500

❌ Please enter a value greater than 0.
```

---

### 📈 8. Interest Breakdown

The result section clearly displays:

* Principal amount
* Rate of interest
* Entered time
* Converted time in years
* Simple Interest
* Simple Interest total amount
* Compound Interest
* Compound Interest total amount
* SI vs CI difference

---

### 💾 9. Calculation History

Every successful calculation is automatically stored in memory.

Users can select:

```text
2. View Calculation History
```

to see previous calculations.

Example:

```text
Calculation #1
----------------------------------------
Currency            : ₹
Principal           : 10,000.00
Rate                : 5.00%
Time                : 2 Years
Simple Interest     : 1,000.00
Simple Amount       : 11,000.00
Compound Interest   : 1,025.00
Compound Amount     : 11,025.00
```

> **Note:** History is stored only while the program is running. It is cleared when the program is closed.

---

## 🛠️ Technologies Used

* **Python 3**
* Python Standard Library
* `math` module

No external Python packages are required.

---

## 📂 Project Structure

```text
Smart-Interest-Calculator/
│
├── interest_calculator.py
└── README.md
```

### `interest_calculator.py`

Contains the complete Python application, including:

* Input validation
* Currency selection
* Time conversion
* Simple Interest calculation
* Compound Interest calculation
* SI vs CI comparison
* Result display
* Calculation history
* Main menu

### `README.md`

Contains the project documentation, features, setup instructions, usage instructions, formulas, and examples.

---

## 💻 Requirements

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

Python **3.8 or above** is recommended.

---

## 🚀 Installation

### Step 1: Clone or Download the Project

Download the project to your computer.

### Step 2: Open the Project Folder

Open Command Prompt, PowerShell, or Terminal inside the project directory.

### Step 3: Run the Program

```bash
python interest_calculator.py
```

On some systems:

```bash
python3 interest_calculator.py
```

---

## ▶️ How to Use

### Step 1: Start the Program

Run:

```bash
python interest_calculator.py
```

### Step 2: Select an Option

```text
==================================================
          💰 SMART INTEREST CALCULATOR
==================================================

📋 MAIN MENU
-----------------------------------
1. 🧮 Calculate Interest
2. 💾 View Calculation History
3. ❌ Exit
-----------------------------------
Enter your choice (1-3):
```

### Step 3: Enter Calculation Details

Select a currency:

```text
1. ₹ INR
2. $ USD
3. € EUR
4. £ GBP
```

Then enter:

```text
Principal amount
Rate of interest
Time
```

and select the time unit.

---

## 🧪 Example

Input:

```text
Currency: ₹ INR
Principal: 10000
Rate: 5
Time: 2 Years
```

Output:

```text
============================================================
                 📊 INTEREST BREAKDOWN
============================================================

--- Input Details ---

Principal Amount       : ₹10,000.00
Rate of Interest       : 5.00%
Time                   : 2 Years
Time in Years          : 2.0000 years

--- Simple Interest ---

Principal              : ₹10,000.00
Simple Interest        : ₹1,000.00
Total Amount           : ₹11,000.00

--- Compound Interest ---

Principal              : ₹10,000.00
Compound Interest      : ₹1,025.00
Total Amount           : ₹11,025.00

--- SI vs CI Comparison ---

Interest Difference    : ₹25.00
Result                 : Compound Interest is higher.
```

---

## 📐 Formulas Used

### Simple Interest

```text
SI = (P × R × T) / 100
```

### Simple Interest Total Amount

```text
A = P + SI
```

### Compound Interest

```text
CI = P(1 + R/100)^T - P
```

### Compound Interest Total Amount

```text
A = P + CI
```

### Time Conversion

For months:

```text
Time in years = Months / 12
```

For days:

```text
Time in years = Days / 365
```

---

## 🧠 Concepts Demonstrated

This project demonstrates several important Python programming concepts:

* Variables
* Data types
* User input
* Type conversion
* Arithmetic operators
* Conditional statements
* Loops
* Functions
* Dictionaries
* Lists
* Exception handling
* String formatting
* Modular programming
* Menu-driven programming
* Basic data storage

---

## 🔍 Error Handling

The application handles invalid input using exception handling.

Example:

```python
try:
    value = float(input(prompt))
except ValueError:
    print("❌ Invalid input. Please enter a number.")
```

This prevents the program from crashing when the user enters text instead of a number.

---

## 📊 Project Workflow

```text
              START
                │
                ↓
          Display Main Menu
                │
       ┌────────┼─────────┐
       ↓        ↓         ↓
 Calculate    History    Exit
 Interest       │         │
       │        ↓         ↓
       │    Show History END
       ↓
 Select Currency
       │
       ↓
 Enter Principal
       │
       ↓
 Enter Interest Rate
       │
       ↓
 Select Time Unit
       │
       ↓
 Enter Time
       │
       ↓
 Convert Time to Years
       │
       ↓
 Calculate Simple Interest
       │
       ↓
 Calculate Compound Interest
       │
       ↓
 Compare SI and CI
       │
       ↓
 Display Breakdown
       │
       ↓
 Save to History
       │
       ↓
 Return to Main Menu
```

---

## 🔮 Future Enhancements

The project can be extended with:

* 🖥️ Tkinter GUI
* 📊 Graphs and charts
* 💾 Save history permanently to CSV
* 📄 Export results to PDF
* 📅 Monthly/quarterly/half-yearly compounding
* 🌙 Dark mode
* 📈 Investment growth visualization
* 🏦 Loan EMI calculator
* 💳 Loan repayment calculator
* 📱 Web version using Flask or Streamlit

---

## 🎯 Project Objective

The main objective of this project is to develop a simple and interactive financial calculator using Python.

It demonstrates how programming concepts such as **functions, loops, conditional statements, exception handling, lists, and dictionaries** can be combined to create a practical application.

---

## 👨‍💻 Author

**Smart Interest Calculator**

Developed as a Python beginner/mini project.

---

## 📜 License

This project is intended for educational and learning purposes.
