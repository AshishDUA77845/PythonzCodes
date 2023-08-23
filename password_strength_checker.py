"""
This script contains functions to check the strength of passwords.
It uses regular expressions and secure input for password evaluation.
"""

import re  # Regular expression support
import getpass  # Secure password input

def is_strong_password(password):
    """
    Check if a password meets strength requirements.

    Parameters:
    password (str): The password to be checked.

    Returns:
    bool: True if the password is strong, False otherwise.
    """
    # Check if the password meets strength requirements.
    # Check length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, digits, and special characters
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = re.search(r"[@_!#$%^&*()<>?/\|}{~:]", password)

    return has_uppercase and has_lowercase and has_digit and has_special

def main():
    """
    Main function to get password input and display result.
    """
    password = getpass.getpass("Enter your password: ")

    if is_strong_password(password):
        print("Strong password! Good job.")
    else:
        print("Weak password. Please make it stronger.")

if __name__ == "__main__":
    main()
