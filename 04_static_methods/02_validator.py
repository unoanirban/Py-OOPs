"""
## Problem 2 — Simple Input Validator

### What you'll learn
- Grouping related utility functions inside a class
- Checking string conditions with simple built-in methods

### Context
A signup form needs to validate user inputs: username, password length,
and email format. These checks don't depend on any object state.

### Requirements
Create a Validator class with these static methods:

1. is_valid_username(username):
   - Returns True if username is at least 3 characters AND only letters/digits.
   - Hint: username.isalnum() checks for letters and digits only.
   - Returns False otherwise.

2. is_valid_password(password):
   - Returns True if password is at least 8 characters long.
   - Returns False otherwise.

3. is_valid_email(email):
   - Returns True if email contains "@" and "."
   - Returns False otherwise.

### Sample Run
print(Validator.is_valid_username("rahul123"))  # True
print(Validator.is_valid_username("rk"))        # False (too short)
print(Validator.is_valid_username("rahul!"))    # False (special character)

print(Validator.is_valid_password("secret12"))  # True
print(Validator.is_valid_password("abc"))       # False

print(Validator.is_valid_email("user@mail.com"))  # True
print(Validator.is_valid_email("notanemail"))      # False

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

