"""-------------------------------------------------------
    GLOBAL FUNCTIONS USED THROUGHOUT PROJECT
-------------------------------------------------------"""


def get_boolean_input(prompt: str) -> bool:
    """---------------------------------------------------
    Return boolean value for user input
    ---------------------------------------------------"""
    # Convert to lowercase for case-insensitivity
    user_input = input(prompt).lower()
    if user_input == "true" or user_input == "yes" or user_input == "1":
        return True
    elif user_input == "false" or user_input == "no" or user_input == "0":
        return False
    else:
        print("Invalid input. Please enter True/False, yes/no, or 1/0!")
        return get_boolean_input(prompt)  # Re-prompt for input


if __name__ == "__main__":
    print("This module is intended for import only")
