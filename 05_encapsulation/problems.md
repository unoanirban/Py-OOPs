# Practice Problems: Encapsulation

Learn how to protect an object's internal data by using private attributes, so that it can only be accessed and modified through controlled methods.

> **Key idea:** Adding double underscores before an attribute name (e.g., `self.__balance`) makes it *private* — it can't be accessed directly from outside the class. You must use methods to get or change it. This is called **encapsulation** — hiding the internal details.

---

## Problem 1 — Bank Account with a Hidden Balance

### Problem Statement
In financial software systems, exposing an account's financial balance as an unprotected public attribute invites accidental modification, bugs, or unauthorized tampering (such as `account.balance = 9999999`). 

To enforce financial integrity, an account's balance must be strictly shielded from direct external access using encapsulation. External callers should only interact with the balance through certified methods (`deposit` and `withdraw`), which rigorously enforce validation rules (rejecting negative transaction amounts and checking against insufficient funds). Direct attribute access from outside the class must be prevented, and reading the balance must be mediated exclusively through a read-only getter method.

### What You'll Learn
- Declaring private attributes using Python's double underscore prefix (`__attribute`)
- Preventing direct external state mutation (name mangling and encapsulation)
- Providing guarded public accessor and mutator methods

### Requirements & Specifications
Create a `BankAccount` class:

1. **Constructor (`__init__`)**:
   - Parameters: `holder`, `initial_balance` (default = `0`)
   - Store the balance as a **private** attribute: `self.__balance`
   - If `initial_balance < 0`, set it to `0` and print `"Balance cannot be negative, set to 0."`

2. **Methods**:
   - `deposit(amount)`:
     - If `amount <= 0`, print `"Deposit must be positive."` and return.
     - Add `amount` to `self.__balance`.
     - Print `"Deposited $<amount>. New balance: $<balance>"`
   - `withdraw(amount)`:
     - If `amount <= 0`, print `"Withdrawal must be positive."` and return.
     - If `amount > self.__balance`, print `"Insufficient funds."` and return.
     - Subtract `amount` from `self.__balance`.
     - Print `"Withdrew $<amount>. New balance: $<balance>"`
   - `get_balance()`:
     - Returns `self.__balance` (this is the only way to check the balance from outside).

### Sample Run
```python
acc = BankAccount("Vikram", 1000)
print(acc.get_balance())   # 1000

acc.deposit(500)           # Deposited $500. New balance: $1500
acc.withdraw(200)          # Withdrew $200. New balance: $1300
print(acc.get_balance())   # 1300

# This would fail — you can't access __balance directly:
# print(acc.__balance)     # AttributeError!
```

---

## Problem 2 — User Account with Password Protection

### Problem Statement
An authentication service manages user credentials for an online service. Storing passwords in cleartext or allowing public access to an account's password attribute represents a critical security vulnerability. 

The user's password must be stored as an encapsulated private attribute that cannot be read directly from the outside. The class must provide a secure verification method that checks whether an attempted password matches the stored credential without exposing the actual password string. Furthermore, updating the password must require two-factor-like validation: the user must supply their valid old password before any change is permitted, and the proposed new password must fulfill minimum length security policies.

### What You'll Learn
- Encapsulating sensitive credentials as private instance variables
- Implementing credential challenge/response verification without leaking secret values
- Enforcing validation workflows and policy checks before permitting credential mutations

### Requirements & Specifications
Create a `UserAccount` class:

1. **Constructor (`__init__`)**:
   - Parameters: `username`, `password`
   - Store password as `self.__password` (private).

2. **Methods**:
   - `verify_password(input_password)`:
     - Returns `True` if `input_password` matches `self.__password`, else `False`.
   - `change_password(old_password, new_password)`:
     - If `old_password` is wrong, print `"Incorrect password."` and return `False`.
     - If `new_password` is less than 6 characters, print `"Password too short (min 6 chars)."` and return `False`.
     - Otherwise, update `self.__password` to `new_password`, print `"Password changed successfully."`, return `True`.
   - `get_username()`:
     - Returns the username (public — that's fine to expose).

### Sample Run
```python
user = UserAccount("rahul_dev", "pass123")
print(user.get_username())             # rahul_dev
print(user.verify_password("pass123")) # True
print(user.verify_password("wrong"))   # False

user.change_password("pass123", "newSecure99")  # Password changed successfully.
print(user.verify_password("newSecure99"))        # True

user.change_password("newSecure99", "abc")  # Password too short (min 6 chars).
```

---

## Problem 3 — Student Grade Book with Data Protection

### Problem Statement
A school learning management system maintains student academic grades across multiple subjects. Academic records are highly sensitive; external scripts or unauthorized callers should never be able to directly overwrite or tamper with the grade dictionary (e.g., executing `grades["Math"] = 100`).

To protect data integrity, the grade records must be stored inside a private dictionary. Grades can only be added through a validated method that ensures scores fall within the legitimate 0–100 scale. If an external client requests the complete set of grades, returning a direct reference to the internal dictionary would allow the caller to mutate it outside the class. Therefore, the class must defend against reference leaks by returning an independent defensive copy of the dictionary, ensuring the internal grade book remains immutable from the outside.

### What You'll Learn
- Protecting collection-based attributes (dictionaries) with private encapsulation
- Validating range boundaries (0–100) before persisting updates
- Preventing reference leaks by returning defensive copies (`dict(...)`)

### Requirements & Specifications
Create a `GradeBook` class:

1. **Constructor (`__init__`)**:
   - Parameter: `student_name`
   - `self.__grades = {}` (private dictionary, subject → score)

2. **Methods**:
   - `add_grade(subject, score)`:
     - If `score < 0` or `score > 100`, print `"Score must be between 0 and 100."` and return.
     - Add the subject and score to `self.__grades`.
   - `get_grade(subject)`:
     - Return the score for that subject, or `None` if not found.
   - `get_average()`:
     - If no grades recorded, return `0`.
     - Otherwise return the average of all scores.
   - `get_all_grades()`:
     - Returns a **copy** of the grades dictionary using `dict(self.__grades)`.
     - **Why a copy?** So that the caller can't modify the internal data by editing the returned dict.

### Sample Run
```python
gb = GradeBook("Ananya")
gb.add_grade("Math", 92)
gb.add_grade("Science", 85)
gb.add_grade("English", 78)

print(gb.get_grade("Math"))     # 92
print(gb.get_average())         # 85.0

grades_copy = gb.get_all_grades()
grades_copy["Math"] = 0         # Try to tamper with it

print(gb.get_grade("Math"))     # Still 92 — the original is safe!
```
