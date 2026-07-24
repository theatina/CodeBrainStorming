import sys
from enum import Enum

class MenuOption(Enum):
    """Enumeration for the interactive CLI menu options."""
    SINGLE_NUMBER = 1
    RANGE_CHECK = 2
    EXIT = 3


def compute_nine_isation(number: int) -> int:
    """
    Collapses a number to 9 by iteratively subtracting the sum of its digits.
    """
    if number <= 0:
        raise ValueError("The algorithm requires a positive integer greater than 0.")

    current_val = number * 10 if number < 9 else number
    
    while current_val != 9:
        temp_val = current_val
        digit_sum = 0
        
        while temp_val > 0:
            temp_val, digit = divmod(temp_val, 10)
            digit_sum += digit
            
        current_val -= digit_sum

    return current_val


def handle_single_number() -> None:
    """Handles the user input and output for checking a single number."""
    try:
        user_input = input("\nType an integer you like: ")
        number = int(user_input)
        
        final_num = compute_nine_isation(number)
        
        if final_num == 9:
            print(f"[SUCCESS] The number {number} successfully collapsed to 9.")
        else:
            print(f"[FAILURE] The number {number} collapsed to {final_num}.")
            
    except ValueError as err:
        # Catches both non-integer inputs and our custom ValueError from the math function
        print(f"\n[ERROR] Invalid input: {err}")


def handle_range_check() -> None:
    """Handles the user input and output for verifying a range of numbers."""
    try:
        user_input = input("\nType a positive integer for the range: ")
        range_limit = int(user_input)
        
        if range_limit <= 0:
            raise ValueError("Range must be greater than 0.")

        print(f"\nChecking all numbers from 1 to {range_limit}. Please wait...")
        
        all_passed = all(compute_nine_isation(i) == 9 for i in range(1, range_limit + 1))

        if all_passed: 
            print(f"[SUCCESS] All integers from 1 up to {range_limit} collapsed to 9.")
        else:
            print(f"[FAILURE] Not all integers in the range collapsed to 9.")
            
    except ValueError as err:
        print(f"\n[ERROR] Invalid input: {err}")


def run_interactive_menu() -> None:
    """Runs the main interactive command-line interface."""
    while True:
        print("\n" + "="*40)
        print("🌀 THE NINE-ISATION OF NUMBERS")
        print("="*40)
        print(f"{MenuOption.SINGLE_NUMBER.value}. Check a single number")
        print(f"{MenuOption.RANGE_CHECK.value}. Verify all integers up to a range")
        print(f"{MenuOption.EXIT.value}. Exit program")
        
        try:
            choice = int(input("\nSelect an option: "))
            menu_selection = MenuOption(choice)
        except ValueError:
            print("\n[ERROR] Please enter a valid number from the menu.")
            continue

        # Route the choice to the appropriate function
        if menu_selection == MenuOption.SINGLE_NUMBER:
            handle_single_number()
        elif menu_selection == MenuOption.RANGE_CHECK:
            handle_range_check()
        elif menu_selection == MenuOption.EXIT:
            print("\nExiting program. Goodbye!\n")
            sys.exit(0)


if __name__ == "__main__":
    try:
        run_interactive_menu()
    except KeyboardInterrupt:
        # Handles the user aggressively quitting the script with Ctrl+C
        print("\n\nProgram interrupted by user. Exiting gracefully...\n")
        sys.exit(0)
