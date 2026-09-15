import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Education",
    "Entertainment",
    "Health",
    "Other"
]


def initialize_file():
    """Create the CSV file if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Category", "Description", "Amount"])


def load_expenses():
    """Load all expenses from the CSV file."""
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_expenses(expenses):
    """Save expenses to the CSV file."""
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["ID", "Date", "Category", "Description", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)


def get_next_id(expenses):
    """Generate the next expense ID."""
    if not expenses:
        return 1

    return max(int(expense["ID"]) for expense in expenses) + 1


def choose_category():
    """Display categories and return the selected category."""
    print("\nCategories:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Choose category: "))

            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]

            print("Invalid category number.")

        except ValueError:
            print("Please enter a valid number.")


def add_expense():
    """Add a new expense."""
    expenses = load_expenses()

    print("\n========== ADD EXPENSE ==========")

    while True:
        try:
            amount = float(input("Enter amount (₹): "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    category = choose_category()

    description = input("Enter description: ").strip()

    if not description:
        description = "No description"

    date = input(
        "Enter date (YYYY-MM-DD) or press Enter for today: "
    ).strip()

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Using today's date.")
            date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "ID": str(get_next_id(expenses)),
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": f"{amount:.2f}"
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")
    print(f"Expense ID: {expense['ID']}")
    print(f"Amount: ₹{expense['Amount']}")


def view_expenses():
    """Display all expenses."""
    expenses = load_expenses()

    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses found.")
        return

    print(
        f"{'ID':<5}"
        f"{'Date':<13}"
        f"{'Category':<17}"
        f"{'Description':<25}"
        f"{'Amount':>12}"
    )

    print("-" * 72)

    for expense in expenses:
        description = expense["Description"]

        if len(description) > 23:
            description = description[:20] + "..."

        print(
            f"{expense['ID']:<5}"
            f"{expense['Date']:<13}"
            f"{expense['Category']:<17}"
            f"{description:<25}"
            f"₹{float(expense['Amount']):>10.2f}"
        )


def total_expenses():
    """Calculate and display total expenses."""
    expenses = load_expenses()

    total = sum(float(expense["Amount"]) for expense in expenses)

    print("\n========== TOTAL EXPENSES ==========")
    print(f"Total money spent: ₹{total:.2f}")


def category_summary():
    """Display expenses grouped by category."""
    expenses = load_expenses()

    print("\n========== CATEGORY SUMMARY ==========")

    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["Category"]
        amount = float(expense["Amount"])

        summary[category] = summary.get(category, 0) + amount

    for category, amount in sorted(summary.items()):
        print(f"{category:<20} ₹{amount:>10.2f}")

    print("-" * 32)

    total = sum(summary.values())

    print(f"{'Total':<20} ₹{total:>10.2f}")


def search_expenses():
    """Search expenses by category or date."""
    expenses = load_expenses()

    print("\n========== SEARCH EXPENSES ==========")

    if not expenses:
        print("No expenses found.")
        return

    print("1. Search by Category")
    print("2. Search by Date")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        search_category = input("Enter category: ").strip().lower()

        results = [
            expense
            for expense in expenses
            if expense["Category"].lower() == search_category
        ]

    elif choice == "2":
        search_date = input("Enter date (YYYY-MM-DD): ").strip()

        results = [
            expense
            for expense in expenses
            if expense["Date"] == search_date
        ]

    else:
        print("Invalid choice.")
        return

    if not results:
        print("No matching expenses found.")
        return

    print("\nMatching Expenses:")
    print("-" * 72)

    for expense in results:
        print(
            f"ID: {expense['ID']} | "
            f"Date: {expense['Date']} | "
            f"Category: {expense['Category']} | "
            f"Description: {expense['Description']} | "
            f"Amount: ₹{float(expense['Amount']):.2f}"
        )


def delete_expense():
    """Delete an expense using its ID."""
    expenses = load_expenses()

    print("\n========== DELETE EXPENSE ==========")

    if not expenses:
        print("No expenses found.")
        return

    expense_id = input("Enter expense ID to delete: ").strip()

    expense_to_delete = None

    for expense in expenses:
        if expense["ID"] == expense_id:
            expense_to_delete = expense
            break

    if expense_to_delete is None:
        print("Expense ID not found.")
        return

    print("\nExpense found:")
    print(f"Date: {expense_to_delete['Date']}")
    print(f"Category: {expense_to_delete['Category']}")
    print(f"Description: {expense_to_delete['Description']}")
    print(f"Amount: ₹{float(expense_to_delete['Amount']):.2f}")

    confirm = input("\nAre you sure you want to delete it? (y/n): ").lower()

    if confirm == "y":
        expenses.remove(expense_to_delete)
        save_expenses(expenses)
        print("Expense deleted successfully!")
    else:
        print("Delete operation cancelled.")


def display_menu():
    """Display the main menu."""
    print("\n")
    print("=" * 40)
    print("          EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Search Expenses")
    print("6. Delete Expense")
    print("7. Exit")
    print("=" * 40)


def main():
    """Main program."""
    initialize_file()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            search_expenses()

        elif choice == "6":
            delete_expense()

        elif choice == "7":
            print("\nThank you for using Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()