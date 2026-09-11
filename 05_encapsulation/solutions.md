# Solutions: 05 — Encapsulation

## Problem 1 — Bank Account with a Hidden Balance

```python
class BankAccount:
    def __init__(self, holder, initial_balance=0):
        if initial_balance < 0:
            print("Balance cannot be negative, set to 0.")
            initial_balance = 0
        self.holder = holder
        self.__balance = initial_balance   # private attribute

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.__balance = self.__balance + amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance = self.__balance - amount
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance   # the only safe way to read the balance


# Try it out
acc = BankAccount("Vikram", 1000)
print(acc.get_balance())   # 1000
acc.deposit(500)           # Deposited $500. New balance: $1500
acc.withdraw(200)          # Withdrew $200. New balance: $1300
print(acc.get_balance())   # 1300

# This would cause an error — can't access __balance directly from outside:
# print(acc.__balance)     # AttributeError!
```

**How it works:**
- `self.__balance` uses Python's **name mangling** — it becomes `_BankAccount__balance` internally, so code outside the class can't easily access it.
- The only way to interact with the balance is through `deposit()`, `withdraw()`, and `get_balance()`.

---

## Problem 2 — User Account with Password Protection

```python
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   # private — never readable from outside

    def verify_password(self, input_password):
        return input_password == self.__password

    def change_password(self, old_password, new_password):
        if not self.verify_password(old_password):
            print("Incorrect password.")
            return False
        if len(new_password) < 6:
            print("Password too short (min 6 chars).")
            return False
        self.__password = new_password
        print("Password changed successfully.")
        return True

    def get_username(self):
        return self.username


# Try it out
user = UserAccount("rahul_dev", "pass123")
print(user.get_username())              # rahul_dev
print(user.verify_password("pass123"))  # True
print(user.verify_password("wrong"))    # False

user.change_password("pass123", "newSecure99")  # Password changed successfully.
print(user.verify_password("newSecure99"))        # True

user.change_password("newSecure99", "abc")  # Password too short (min 6 chars).
```

**How it works:**
- `self.__password` is private — you can never do `user.__password` from outside.
- `verify_password` uses `self.__password` internally to compare.
- `change_password` calls `self.verify_password(old_password)` first — reusing a method inside the class.

---

## Problem 3 — Student Grade Book with Data Protection

```python
class GradeBook:
    def __init__(self, student_name):
        self.student_name = student_name
        self.__grades = {}   # private dictionary

    def add_grade(self, subject, score):
        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            return
        self.__grades[subject] = score

    def get_grade(self, subject):
        return self.__grades.get(subject, None)

    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        total = sum(self.__grades.values())
        return total / len(self.__grades)

    def get_all_grades(self):
        return dict(self.__grades)   # return a COPY, not the original


# Try it out
gb = GradeBook("Ananya")
gb.add_grade("Math", 92)
gb.add_grade("Science", 85)
gb.add_grade("English", 78)
gb.add_grade("Art", 110)   # Score must be between 0 and 100.

print(gb.get_grade("Math"))   # 92
print(gb.get_average())       # 85.0

grades_copy = gb.get_all_grades()
grades_copy["Math"] = 0       # modifying the copy...

print(gb.get_grade("Math"))   # Still 92! The original is safe.
```

**How it works:**
- `self.__grades` is private — no external code can do `gb.__grades["Math"] = 0`.
- `get_all_grades()` returns `dict(self.__grades)` — a brand new copy of the dictionary. Modifying the copy doesn't affect the original.
- This technique is called **defensive copying**.
