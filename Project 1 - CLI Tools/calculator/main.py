# calculator/main.py

from operations import add, subtract, multiply, divide
from history import load_history, add_to_history, clear_history
from utils import print_menu, get_float_input
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define the header/banner
HEADER = rf"""
{Fore.CYAN}{'='*40}
     ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
    ██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
    ██║   ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
    ██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
    ╚██████╔╝██║ ╚████║   ██║   ██╔╝ ██╗
     ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝     
{Fore.CYAN}{'='*40}
{Fore.YELLOW}     Welcome to the Calculator CLI!
{Fore.CYAN}{'='*40}
"""


def display_history() -> None:
    """Print the full history of calculations in color."""
    history = load_history()
    if not history:
        print(Fore.YELLOW + "No history found.")
        return
    print(Fore.CYAN + "\n--- Calculation History ---")
    for idx, entry in enumerate(history, start=1):
        print(
            f"{Fore.MAGENTA}{idx}. {entry['operation'].title()} {entry['a']} and {entry['b']} = {entry['result']}"
        )


def perform_operation(choice: int) -> None:
    """Perform selected math operation based on user choice with colored results/errors."""
    ops = {
        1: ("add", add),
        2: ("subtract", subtract),
        3: ("multiply", multiply),
        4: ("divide", divide),
    }

    op_name, func = ops[choice]
    a = get_float_input("Enter first number: ")
    b = get_float_input("Enter second number: ")

    try:
        result = func(a, b)
        print(f"{Fore.GREEN}Result: {result}")
        add_to_history(op_name, a, b, result)
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}")


def main() -> None:
    """Main CLI loop with colored prompts and outputs."""
    try:
        print(HEADER)  # Print the header on startup
        while True:
            print_menu()
            try:
                choice = int(input(Fore.BLUE + "Select an option (1-7): "))
                if choice == 7:
                    print(Fore.GREEN + "Goodbye!")
                    break
                elif 1 <= choice <= 4:
                    perform_operation(choice)
                elif choice == 5:
                    display_history()
                elif choice == 6:
                    clear_history()
                    print(Fore.YELLOW + "History cleared.")
                else:
                    print(Fore.RED + "Invalid choice. Please select 1-7.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nUser Exited! Clearing Up resources!")


if __name__ == "__main__":
    main()