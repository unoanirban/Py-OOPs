# Solutions: 04 — Static Methods

## Problem 1 — Temperature Converter

```python
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15


# Try it out — no object creation needed!
print(TemperatureConverter.celsius_to_fahrenheit(100))   # 212.0
print(TemperatureConverter.fahrenheit_to_celsius(32))    # 0.0
print(TemperatureConverter.celsius_to_kelvin(25))        # 298.15
print(TemperatureConverter.kelvin_to_celsius(0))         # -273.15
```

**How it works:**
- `@staticmethod` means the method doesn't receive `self` or `cls`.
- It's just a regular function inside the class for organisation.
- We call it as `TemperatureConverter.celsius_to_fahrenheit(100)` — no object needed.

---

## Problem 2 — Simple Input Validator

```python
class Validator:

    @staticmethod
    def is_valid_username(username):
        if len(username) < 3:
            return False
        if not username.isalnum():
            return False
        return True

    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email


# Try it out
print(Validator.is_valid_username("rahul123"))  # True
print(Validator.is_valid_username("rk"))        # False
print(Validator.is_valid_username("rahul!"))    # False

print(Validator.is_valid_password("secret12"))  # True
print(Validator.is_valid_password("abc"))       # False

print(Validator.is_valid_email("user@mail.com"))  # True
print(Validator.is_valid_email("notanemail"))      # False
```

**How it works:**
- Each validator is a self-contained function — no object state involved.
- `isalnum()` is a built-in Python string method: returns `True` if all characters are letters or digits.
- Grouping them inside `Validator` makes the code organised and readable.

---

## Problem 3 — Math Utility

```python
class MathUtil:

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        if n < 0:
            print("Factorial not defined for negative numbers")
            return None
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result

    @staticmethod
    def max_of_two(a, b):
        if a >= b:
            return a
        return b


# Try it out
print(MathUtil.is_prime(7))     # True
print(MathUtil.is_prime(10))    # False
print(MathUtil.is_prime(1))     # False

print(MathUtil.factorial(5))    # 120
print(MathUtil.factorial(0))    # 1
print(MathUtil.factorial(-3))   # Factorial not defined for negative numbers

print(MathUtil.max_of_two(10, 25))   # 25
print(MathUtil.max_of_two(7, 7))     # 7
```

**How it works:**
- `is_prime` loops from 2 to n-1. If n is divisible by any number in that range, it's not prime.
- `factorial` uses a loop and a running `result` variable, multiplying it by each number from 1 to n.
- `max_of_two` is the simplest possible comparison — no Python built-in `max()` needed here.
