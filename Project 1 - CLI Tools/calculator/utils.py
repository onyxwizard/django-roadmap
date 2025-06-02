# calculator/utils.py

def print_menu() -> None:
    """Display the user menu."""
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")


def get_float_input(prompt: str) -> float:
    """Prompt for a float input, handle invalid entries."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")