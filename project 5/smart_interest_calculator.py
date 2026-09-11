# ============================================================
#              SMART INTEREST CALCULATOR
# ============================================================
# Features:
# 1. Simple Interest
# 2. Compound Interest
# 3. SI vs CI Comparison
# 4. Years / Months / Days
# 5. Currency Selection
# 6. Multiple Calculations
# 7. Input Validation
# 8. Interest Breakdown
# 9. Calculation History
# ============================================================

import math


# ------------------------------------------------------------
# Currency Options
# ------------------------------------------------------------

CURRENCIES = {
    "1": ("₹", "INR"),
    "2": ("$", "USD"),
    "3": ("€", "EUR"),
    "4": ("£", "GBP")
}


# ------------------------------------------------------------
# Calculation History
# ------------------------------------------------------------

history = []


# ------------------------------------------------------------
# Get Positive Number
# ------------------------------------------------------------

def get_positive_number(prompt):
    """Get a valid positive number from the user."""

    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("❌ Please enter a value greater than 0.")

            else:
                return value

        except ValueError:
            print("❌ Invalid input. Please enter a number.")


# ------------------------------------------------------------
# Currency Selection
# ------------------------------------------------------------

def choose_currency():
    """Allow the user to select a currency."""

    print("\n💰 SELECT CURRENCY")
    print("-" * 30)
    print("1. ₹ INR")
    print("2. $ USD")
    print("3. € EUR")
    print("4. £ GBP")

    while True:

        choice = input("Enter your choice (1-4): ")

        if choice in CURRENCIES:
            return CURRENCIES[choice]

        print("❌ Invalid currency choice. Please select 1-4.")


# ------------------------------------------------------------
# Time Unit Selection
# ------------------------------------------------------------

def choose_time_unit():
    """Allow the user to select the time unit."""

    print("\n📅 SELECT TIME UNIT")
    print("-" * 30)
    print("1. Years")
    print("2. Months")
    print("3. Days")

    while True:

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "Years"

        elif choice == "2":
            return "Months"

        elif choice == "3":
            return "Days"

        print("❌ Invalid choice. Please select 1-3.")


# ------------------------------------------------------------
# Convert Time to Years
# ------------------------------------------------------------

def convert_to_years(time, unit):
    """Convert months or days into years."""

    if unit == "Years":
        return time

    elif unit == "Months":
        return time / 12

    elif unit == "Days":
        return time / 365


# ------------------------------------------------------------
# Simple Interest
# ------------------------------------------------------------

def calculate_simple_interest(principal, rate, time_years):
    """
    Simple Interest Formula:

    SI = (P × R × T) / 100
    """

    return (principal * rate * time_years) / 100


# ------------------------------------------------------------
# Compound Interest
# ------------------------------------------------------------

def calculate_compound_interest(principal, rate, time_years):
    """
    Compound Interest Formula:

    CI = P(1 + R/100)^T - P

    Compounding is done annually.
    """

    amount = principal * math.pow(
        1 + rate / 100,
        time_years
    )

    compound_interest = amount - principal

    return compound_interest


# ------------------------------------------------------------
# Display Results
# ------------------------------------------------------------

def display_results(
    principal,
    rate,
    original_time,
    time_unit,
    time_years,
    simple_interest,
    simple_amount,
    compound_interest,
    compound_amount,
    currency
):

    symbol = currency[0]

    difference = compound_interest - simple_interest

    print("\n" + "=" * 60)
    print("                 📊 INTEREST BREAKDOWN")
    print("=" * 60)

    # Basic information

    print("\n--- Input Details ---")

    print(
        f"Principal Amount       : "
        f"{symbol}{principal:,.2f}"
    )

    print(
        f"Rate of Interest       : "
        f"{rate:.2f}%"
    )

    print(
        f"Time                   : "
        f"{original_time:g} {time_unit}"
    )

    print(
        f"Time in Years          : "
        f"{time_years:.4f} years"
    )

    # Simple Interest

    print("\n--- Simple Interest ---")

    print(
        f"Principal              : "
        f"{symbol}{principal:,.2f}"
    )

    print(
        f"Simple Interest        : "
        f"{symbol}{simple_interest:,.2f}"
    )

    print(
        f"Total Amount           : "
        f"{symbol}{simple_amount:,.2f}"
    )

    # Compound Interest

    print("\n--- Compound Interest ---")

    print(
        f"Principal              : "
        f"{symbol}{principal:,.2f}"
    )

    print(
        f"Compound Interest      : "
        f"{symbol}{compound_interest:,.2f}"
    )

    print(
        f"Total Amount           : "
        f"{symbol}{compound_amount:,.2f}"
    )

    # Comparison

    print("\n--- SI vs CI Comparison ---")

    print(
        f"Interest Difference    : "
        f"{symbol}{abs(difference):,.2f}"
    )

    if compound_interest > simple_interest:

        print(
            "Result                 : "
            "Compound Interest is higher."
        )

    elif simple_interest > compound_interest:

        print(
            "Result                 : "
            "Simple Interest is higher."
        )

    else:

        print(
            "Result                 : "
            "Both interests are equal."
        )

    print("=" * 60)


# ------------------------------------------------------------
# Save Calculation to History
# ------------------------------------------------------------

def save_to_history(
    principal,
    rate,
    original_time,
    time_unit,
    simple_interest,
    simple_amount,
    compound_interest,
    compound_amount,
    currency
):

    history.append({

        "currency": currency[0],

        "principal": principal,

        "rate": rate,

        "time": original_time,

        "time_unit": time_unit,

        "simple_interest": simple_interest,

        "simple_amount": simple_amount,

        "compound_interest": compound_interest,

        "compound_amount": compound_amount

    })


# ------------------------------------------------------------
# Display History
# ------------------------------------------------------------

def show_history():

    print("\n" + "=" * 70)
    print("                  💾 CALCULATION HISTORY")
    print("=" * 70)

    if not history:

        print("\nNo calculation history available.")

        print("=" * 70)

        return

    for index, record in enumerate(history, start=1):

        print(f"\nCalculation #{index}")
        print("-" * 40)

        print(
            f"Currency            : "
            f"{record['currency']}"
        )

        print(
            f"Principal           : "
            f"{record['principal']:,.2f}"
        )

        print(
            f"Rate                : "
            f"{record['rate']:.2f}%"
        )

        print(
            f"Time                : "
            f"{record['time']:g} "
            f"{record['time_unit']}"
        )

        print(
            f"Simple Interest     : "
            f"{record['simple_interest']:,.2f}"
        )

        print(
            f"Simple Amount       : "
            f"{record['simple_amount']:,.2f}"
        )

        print(
            f"Compound Interest   : "
            f"{record['compound_interest']:,.2f}"
        )

        print(
            f"Compound Amount     : "
            f"{record['compound_amount']:,.2f}"
        )

    print("\n" + "=" * 70)


# ------------------------------------------------------------
# Perform New Calculation
# ------------------------------------------------------------

def perform_calculation():

    print("\n" + "=" * 50)
    print("                 🧮 NEW CALCULATION")
    print("=" * 50)

    # Currency

    currency = choose_currency()

    # Principal

    principal = get_positive_number(
        "\nEnter principal amount: "
    )

    # Rate

    rate = get_positive_number(
        "Enter rate of interest (%): "
    )

    # Time Unit

    time_unit = choose_time_unit()

    # Time

    original_time = get_positive_number(
        f"Enter time in {time_unit.lower()}: "
    )

    # Convert time to years

    time_years = convert_to_years(
        original_time,
        time_unit
    )

    # Calculate Simple Interest

    simple_interest = calculate_simple_interest(
        principal,
        rate,
        time_years
    )

    simple_amount = principal + simple_interest

    # Calculate Compound Interest

    compound_interest = calculate_compound_interest(
        principal,
        rate,
        time_years
    )

    compound_amount = principal + compound_interest

    # Display Results

    display_results(
        principal,
        rate,
        original_time,
        time_unit,
        time_years,
        simple_interest,
        simple_amount,
        compound_interest,
        compound_amount,
        currency
    )

    # Save Calculation

    save_to_history(
        principal,
        rate,
        original_time,
        time_unit,
        simple_interest,
        simple_amount,
        compound_interest,
        compound_amount,
        currency
    )

    print("\n✅ Calculation saved to history.")


# ------------------------------------------------------------
# Main Menu
# ------------------------------------------------------------

def main():

    while True:

        print("\n")
        print("=" * 50)
        print("          💰 SMART INTEREST CALCULATOR")
        print("=" * 50)

        print("\n📋 MAIN MENU")
        print("-" * 35)

        print("1. 🧮 Calculate Interest")
        print("2. 💾 View Calculation History")
        print("3. ❌ Exit")

        print("-" * 35)

        choice = input(
            "Enter your choice (1-3): "
        )

        if choice == "1":

            perform_calculation()

        elif choice == "2":

            show_history()

        elif choice == "3":

            print("\n" + "=" * 50)
            print("👋 Thank you for using")
            print("   Smart Interest Calculator!")
            print("=" * 50)

            break

        else:

            print(
                "\n❌ Invalid choice. "
                "Please select 1, 2, or 3."
            )


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------

if __name__ == "__main__":
    main()