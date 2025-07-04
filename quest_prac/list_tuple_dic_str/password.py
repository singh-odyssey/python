"""
Password Validator

Checking if the password is valid or not based on the following conditions:
1. Contains at least one uppercase letter
2. Contains at least one lowercase letter
3. Contains at least one digit
4. Contains at least one special character (e.g., !@#$%^&*()-_=+[]{}|;:'",.<>?/)
5. Length must be between 6 and 12 characters
"""

# Constants
MINIMUM_PASSWORD_LENGTH = 6
MAXIMUM_PASSWORD_LENGTH = 12
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"


def is_valid_password(password):

    # Check password length
    if len(password) < MINIMUM_PASSWORD_LENGTH or len(password) > MAXIMUM_PASSWORD_LENGTH:
        print(f"Password length must be between {MINIMUM_PASSWORD_LENGTH} and {MAXIMUM_PASSWORD_LENGTH} characters")
        return False
    
    # Check for uppercase letter
    if not any(c.isupper() for c in password):
        print("Password must contain at least one uppercase letter")
        return False
    
    # Check for lowercase letter
    if not any(c.islower() for c in password):
        print("Password must contain at least one lowercase letter")
        return False
    
    # Check for digit
    if not any(c.isdigit() for c in password):
        print("Password must contain at least one digit")
        return False
    
    # Check for special character
    if not any(c in SPECIAL_CHARACTERS for c in password):
        print("Password must contain at least one special character")
        return False
    
    print("Password is valid!")
    return True


def main():
    """Main function to get user input and validate multiple passwords separated by commas."""
    passwords_input = input("Enter passwords separated by commas -> ")
    passwords = [p.strip() for p in passwords_input.split(',')]
    print("\nValid passwords:")
    any_valid = False
    for password in passwords:
        if is_valid_password(password):
            print(password)
            any_valid = True
    if not any_valid:
        print("No valid passwords found.")


if __name__ == "__main__":
    main()