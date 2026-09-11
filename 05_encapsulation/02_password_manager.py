"""
## Problem 2 — User Account with Password Protection

### What you'll learn
- Private attributes for sensitive data (passwords)
- Validating old credentials before allowing changes

### Context
A user account stores a username and password. The password is private.
To change it, you must provide the old password first.

### Requirements
Create a UserAccount class:

1. Constructor (__init__):
   - Parameters: username, password
   - Store password as self.__password (private).

2. Methods:
   - verify_password(input_password):
       Returns True if input_password matches self.__password, else False.

   - change_password(old_password, new_password):
       If old_password is wrong, print "Incorrect password." and return False.
       If new_password is less than 6 characters, print "Password too short (min 6 chars)." and return False.
       Otherwise update self.__password, print "Password changed successfully.", return True.

   - get_username():
       Returns the username.

### Sample Run
user = UserAccount("rahul_dev", "pass123")
print(user.get_username())              # rahul_dev
print(user.verify_password("pass123"))  # True
print(user.verify_password("wrong"))    # False
user.change_password("pass123", "newSecure99")  # Password changed successfully.
print(user.verify_password("newSecure99"))        # True

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

