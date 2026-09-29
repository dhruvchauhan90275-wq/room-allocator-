"""
Input Validation Module
Ensures CLI input reliability without application crashes.
"""


def get_non_negative_integer(prompt):
    """Prompts until a valid non-negative integer (>= 0) is entered."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val >= 0:
                return val
            print("Error: Input must be a non-negative integer (0 or greater).")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")


def get_positive_integer(prompt):
    """Prompts until a valid positive integer (> 0) is entered."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val > 0:
                return val
            print("Error: Input must be a positive integer greater than zero.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")


def get_non_empty_string(prompt):
    """Prompts until a non-empty string is entered."""
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Error: Field cannot be left blank.")


def get_menu_choice(prompt, min_val, max_val):
    """Prompts for an integer choice within [min_val, max_val]."""
    while True:
        try:
            val = int(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"Error: Please choose a valid option between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")


def get_yes_no(prompt):
    """Prompts for a y/n response."""
    while True:
        val = input(prompt).strip().lower()
        if val in ['y', 'yes']:
            return True
        if val in ['n', 'no']:
            return False
        print("Error: Please enter 'y' for yes or 'n' for no.")