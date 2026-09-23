"""
ATM Simulation
--------------
A beginner-friendly console-based ATM simulation using Python and JSON.

Features:
- PIN authentication
- Check balance
- Deposit money
- Withdraw money
- Change PIN
- Transaction history
- JSON-based account persistence
"""

import json
from datetime import datetime
from pathlib import Path

ACCOUNT_FILE = Path(__file__).with_name("account.json")
MAX_PIN_ATTEMPTS = 3


def load_account():
    """Load account information from account.json."""
    try:
        with ACCOUNT_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: account.json was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: account.json contains invalid JSON.")
        return None


def save_account(account):
    """Save updated account information to account.json."""
    with ACCOUNT_FILE.open("w", encoding="utf-8") as file:
        json.dump(account, file, indent=4)


def add_transaction(account, transaction_type, amount, balance_after):
    """Add a transaction record with the current date and time."""
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": transaction_type,
        "amount": round(amount, 2),
        "balance_after": round(balance_after, 2),
    }
    account.setdefault("transactions", []).append(transaction)


def authenticate(account):
    """Authenticate the user using the account PIN."""
    for attempt in range(1, MAX_PIN_ATTEMPTS + 1):
        pin = input("Enter your 4-digit PIN: ").strip()

        if pin == str(account["pin"]):
            print(f"\nWelcome, {account['name']}!")
            return True

        remaining = MAX_PIN_ATTEMPTS - attempt
        if remaining:
            print(f"Incorrect PIN. Attempts remaining: {remaining}")
        else:
            print("Too many incorrect attempts. Access denied.")

    return False


def get_positive_amount(prompt):
    """Get a valid positive amount from the user."""
    while True:
        value = input(prompt).strip()

        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a valid numeric amount.")


def check_balance(account):
    """Display the current account balance."""
    print(f"\nCurrent balance: ₹{account['balance']:.2f}")


def deposit(account):
    """Deposit money into the account."""
    amount = get_positive_amount("Enter deposit amount: ₹")
    account["balance"] += amount
    account["balance"] = round(account["balance"], 2)

    add_transaction(account, "Deposit", amount, account["balance"])
    save_account(account)

    print(f"₹{amount:.2f} deposited successfully.")
    print(f"New balance: ₹{account['balance']:.2f}")


def withdraw(account):
    """Withdraw money if sufficient balance is available."""
    amount = get_positive_amount("Enter withdrawal amount: ₹")

    if amount > account["balance"]:
        print("Insufficient balance.")
        return

    account["balance"] -= amount
    account["balance"] = round(account["balance"], 2)

    add_transaction(account, "Withdrawal", amount, account["balance"])
    save_account(account)

    print(f"Please collect your cash: ₹{amount:.2f}")
    print(f"Remaining balance: ₹{account['balance']:.2f}")


def change_pin(account):
    """Change the account PIN after validating the old PIN."""
    old_pin = input("Enter current PIN: ").strip()

    if old_pin != str(account["pin"]):
        print("Incorrect current PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()

    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("PIN must contain exactly 4 digits.")
        return

    confirm_pin = input("Confirm new PIN: ").strip()

    if new_pin != confirm_pin:
        print("PIN confirmation does not match.")
        return

    if new_pin == str(account["pin"]):
        print("New PIN must be different from the current PIN.")
        return

    account["pin"] = new_pin
    save_account(account)
    print("PIN changed successfully.")


def show_transactions(account):
    """Display the transaction history."""
    transactions = account.get("transactions", [])

    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n" + "=" * 65)
    print("                    TRANSACTION HISTORY")
    print("=" * 65)

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index}. {transaction['date']} | "
            f"{transaction['type']:<12} | "
            f"₹{transaction['amount']:>10.2f} | "
            f"Balance: ₹{transaction['balance_after']:>10.2f}"
        )

    print("=" * 65)


def display_menu():
    """Display the main ATM menu."""
    print("\n" + "=" * 40)
    print("           ATM SIMULATION")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")
    print("=" * 40)


def main():
    """Run the ATM simulation."""
    print("=" * 40)
    print("       WELCOME TO ATM SIMULATION")
    print("=" * 40)

    account = load_account()

    if account is None:
        return

    if not authenticate(account):
        return

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            check_balance(account)

        elif choice == "2":
            deposit(account)

        elif choice == "3":
            withdraw(account)

        elif choice == "4":
            change_pin(account)

        elif choice == "5":
            show_transactions(account)

        elif choice == "6":
            print("\nThank you for using the ATM.")
            print("Please collect your card. Have a great day!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
