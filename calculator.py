"""
Simple Python Calculator
Supports addition, subtraction, multiplication, division, exponentiation,
modulus, and square root.
"""

import math


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b, preventing division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def modulus(a, b):
    """Return the remainder after dividing a by b."""
    if b == 0:
        raise ValueError("Cannot calculate modulus with zero.")
    return a % b


def square_root(a):
    """Return the square root of a, for non-negative numbers."""
    if a < 0:
        raise ValueError("Cannot calculate the real square root of a negative number.")
    return math.sqrt(a)


def get_number(prompt):
    """Prompt until the user enters a valid number."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Please enter a valid number.")


def format_result(value):
    """Display whole-number results without an unnecessary decimal part."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def main():
    operations = {
        "1": ("Addition (+)", add, 2),
        "2": ("Subtraction (-)", subtract, 2),
        "3": ("Multiplication (*)", multiply, 2),
        "4": ("Division (/)", divide, 2),
        "5": ("Power (a ** b)", power, 2),
        "6": ("Modulus (remainder)", modulus, 2),
        "7": ("Square root (√a)", square_root, 1),
    }

    print("=" * 34)
    print("       PYTHON CALCULATOR")
    print("=" * 34)

    while True:
        print("\nChoose an operation:")
        for key, (label, _, _) in operations.items():
            print(f"{key}. {label}")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Calculator closed. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Select an option from the menu.")
            continue

        label, operation, number_count = operations[choice]
        first = get_number("Enter a number: ")

        if number_count == 2:
            second = get_number("Enter the second number: ")
            try:
                result = operation(first, second)
            except (ValueError, OverflowError) as error:
                print(f"Error: {error}")
                continue
        else:
            try:
                result = operation(first)
            except (ValueError, OverflowError) as error:
                print(f"Error: {error}")
                continue

        print(f"Result ({label}): {format_result(result)}")


if __name__ == "__main__":
    main()
