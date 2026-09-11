"""
Unit Converter
A simple command-line unit converter supporting length, weight, temperature,
time, volume, and digital data conversions.

Run:
    python unit_converter.py
"""

from __future__ import annotations

from typing import Callable, Dict


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Convert length using meters as the base unit."""
    factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
    }
    return value * factors[from_unit] / factors[to_unit]


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    """Convert weight/mass using grams as the base unit."""
    factors = {
        "mg": 0.001,
        "g": 1.0,
        "kg": 1000.0,
        "oz": 28.349523125,
        "lb": 453.59237,
    }
    return value * factors[from_unit] / factors[to_unit]


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature through Celsius."""
    if from_unit == to_unit:
        return value

    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        raise ValueError("Invalid temperature unit.")

    if to_unit == "c":
        return celsius
    if to_unit == "f":
        return (celsius * 9 / 5) + 32
    if to_unit == "k":
        return celsius + 273.15

    raise ValueError("Invalid temperature unit.")


def convert_time(value: float, from_unit: str, to_unit: str) -> float:
    """Convert time using seconds as the base unit."""
    factors = {
        "s": 1.0,
        "min": 60.0,
        "h": 3600.0,
        "day": 86400.0,
    }
    return value * factors[from_unit] / factors[to_unit]


def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    """Convert volume using liters as the base unit."""
    factors = {
        "ml": 0.001,
        "l": 1.0,
        "tsp": 0.00492892159375,
        "tbsp": 0.01478676478125,
        "cup": 0.2365882365,
        "gal": 3.785411784,
    }
    return value * factors[from_unit] / factors[to_unit]


def convert_data(value: float, from_unit: str, to_unit: str) -> float:
    """Convert digital data using bytes as the base unit."""
    factors = {
        "b": 1.0,
        "kb": 1024.0,
        "mb": 1024.0**2,
        "gb": 1024.0**3,
        "tb": 1024.0**4,
    }
    return value * factors[from_unit] / factors[to_unit]


CATEGORIES: Dict[str, Dict[str, object]] = {
    "length": {
        "units": ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"],
        "convert": convert_length,
    },
    "weight": {
        "units": ["mg", "g", "kg", "oz", "lb"],
        "convert": convert_weight,
    },
    "temperature": {
        "units": ["c", "f", "k"],
        "convert": convert_temperature,
    },
    "time": {
        "units": ["s", "min", "h", "day"],
        "convert": convert_time,
    },
    "volume": {
        "units": ["ml", "l", "tsp", "tbsp", "cup", "gal"],
        "convert": convert_volume,
    },
    "data": {
        "units": ["b", "kb", "mb", "gb", "tb"],
        "convert": convert_data,
    },
}


def format_number(value: float) -> str:
    """Return a clean representation for display."""
    if abs(value) < 1e-12:
        value = 0.0

    if value.is_integer():
        return str(int(value))

    return f"{value:.10f}".rstrip("0").rstrip(".")


def display_categories() -> None:
    print("\nAvailable categories:")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category.title()}")


def choose_category() -> str | None:
    display_categories()

    while True:
        choice = input("\nChoose a category (1-6) or Q to quit: ").strip().lower()

        if choice == "q":
            return None

        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return list(CATEGORIES.keys())[int(choice) - 1]

        print("Invalid choice. Please select a number from 1 to 6.")


def choose_unit(category: str, prompt: str) -> str:
    units = CATEGORIES[category]["units"]

    print(f"\nAvailable units for {category.title()}:")
    print(" | ".join(units))

    while True:
        unit = input(prompt).strip().lower()

        if unit in units:
            return unit

        print(f"Invalid unit. Choose one of: {', '.join(units)}")


def get_value() -> float:
    while True:
        raw_value = input("Enter value: ").strip()

        try:
            return float(raw_value)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def perform_conversion() -> None:
    category = choose_category()

    if category is None:
        print("\nThank you for using Unit Converter!")
        return

    from_unit = choose_unit(category, "From unit: ")
    to_unit = choose_unit(category, "To unit: ")
    value = get_value()

    converter: Callable[[float, str, str], float] = CATEGORIES[category]["convert"]  # type: ignore
    result = converter(value, from_unit, to_unit)

    print("\n" + "=" * 45)
    print(
        f"{format_number(value)} {from_unit} = "
        f"{format_number(result)} {to_unit}"
    )
    print("=" * 45)


def main() -> None:
    print("=" * 45)
    print("        UNIT CONVERTER")
    print("=" * 45)

    while True:
        perform_conversion()

        again = input("\nDo you want to convert again? (y/n): ").strip().lower()

        if again != "y":
            print("\nThank you for using Unit Converter!")
            break


if __name__ == "__main__":
    main()
