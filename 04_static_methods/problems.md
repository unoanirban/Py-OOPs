# Practice Problems: Static Methods

Learn when to use `@staticmethod` — for utility functions that logically belong to a class but don't need access to any instance (`self`) or class (`cls`) data.

> **Key idea:** A *static method* is just a regular function that lives inside a class for organisation. It doesn't receive `self` or `cls`. Use it for helper/utility functions that are related to the class but don't depend on any specific object.

---

## Problem 1 — Temperature Converter

### Problem Statement
A meteorological station and weather forecast application processes temperature data collected across diverse instruments. Some sensors report readings in degrees Celsius, others in Fahrenheit, and laboratory equipment records absolute temperatures in Kelvin.

Because physical temperature conversion equations represent pure mathematical formulas that do not depend on the state of any individual weather station or sensor instance, creating instances of a converter class would incur unnecessary memory overhead. Your task is to design a cohesive `TemperatureConverter` utility class containing stateless static methods capable of converting temperatures back and forth between Celsius, Fahrenheit, and Kelvin.

### What You'll Learn
- Defining `@staticmethod` methods inside a class namespace
- Invoking utility methods directly on the class without instantiating objects
- Encapsulating domain-specific conversion formulas into an organized namespace

### Requirements & Specifications
Create a `TemperatureConverter` class with the following static methods:

1. `celsius_to_fahrenheit(c)`:
   - Formula: `(c * 9/5) + 32`
   - Returns the result.

2. `fahrenheit_to_celsius(f)`:
   - Formula: `(f - 32) * 5/9`
   - Returns the result.

3. `celsius_to_kelvin(c)`:
   - Formula: `c + 273.15`
   - Returns the result.

4. `kelvin_to_celsius(k)`:
   - Formula: `k - 273.15`
   - Returns the result.

### Sample Run
```python
print(TemperatureConverter.celsius_to_fahrenheit(100))   # 212.0
print(TemperatureConverter.fahrenheit_to_celsius(32))    # 0.0
print(TemperatureConverter.celsius_to_kelvin(25))        # 298.15
print(TemperatureConverter.kelvin_to_celsius(0))         # -273.15
```

> Notice: we call these methods directly on the class — no `TemperatureConverter()` object needed!

---

## Problem 2 — Simple Input Validator

### Problem Statement
A web registration portal handles thousands of user signups daily. Before persisting user profiles to the database, incoming form inputs must be sanitized and validated against standard security and formatting policies:
- Usernames must satisfy minimum length constraints and contain only alphanumeric characters to prevent script injections.
- Passwords must satisfy basic length thresholds to ensure account security.
- Email strings must contain essential structural markers (`@` and `.`).

These validation rules are stateless predicate functions: they take raw string inputs and return boolean results (`True` or `False`). You need to group these related validation utilities into a single `Validator` class using static methods for easy reuse across different controllers and services.

### What You'll Learn
- Grouping related helper and validation functions under a shared class namespace
- Leveraging Python's built-in string methods (like `.isalnum()`) within static methods
- Writing clear boolean predicates for form validation logic

### Requirements & Specifications
Create a `Validator` class with the following static methods:

1. `is_valid_username(username)`:
   - Returns `True` if `username` is at least 3 characters long and contains only letters and digits.
   - Hint: use `username.isalnum()` to check for letters/digits only.
   - Returns `False` otherwise.

2. `is_valid_password(password)`:
   - Returns `True` if `password` is at least 8 characters long.
   - Returns `False` otherwise.

3. `is_valid_email(email)`:
   - A simple check: returns `True` if `email` contains `"@"` and `"."`.
   - Returns `False` otherwise.

### Sample Run
```python
print(Validator.is_valid_username("rahul123"))  # True
print(Validator.is_valid_username("rk"))        # False (too short)
print(Validator.is_valid_username("rahul!"))    # False (special character)

print(Validator.is_valid_password("secret12"))  # True
print(Validator.is_valid_password("abc"))       # False

print(Validator.is_valid_email("user@mail.com"))  # True
print(Validator.is_valid_email("notanemail"))      # False
```

---

## Problem 3 — Math Utility

### Problem Statement
An educational math application requires a collection of common numeric operations to support interactive classroom exercises and student quizzes. The system requires standard mathematical routines including checking whether an integer is prime, computing the factorial of non-negative numbers, and determining the maximum of two numerical values.

Because these operations are purely functional calculations that do not preserve historical state or configure unique object properties, they belong together in a dedicated `MathUtil` class composed of static methods. The methods must also handle mathematical edge cases gracefully (such as prime status for numbers `<= 1` and factorials for negative inputs).

### What You'll Learn
- Writing iterative algorithms (primality checking, factorial multiplication) inside static methods
- Handling domain edge cases and invalid arithmetic boundaries (e.g., negative factorials)
- Designing a reusable mathematical utility class

### Requirements & Specifications
Create a `MathUtil` class with the following static methods:

1. `is_prime(n)`:
   - Returns `False` if `n <= 1`.
   - Returns `True` if `n` is only divisible by 1 and itself.
   - Hint: loop from `2` to `n-1`, check if `n % i == 0`.

2. `factorial(n)`:
   - Returns `1` if `n == 0`.
   - If `n < 0`, print `"Factorial not defined for negative numbers"` and return `None`.
   - Otherwise, compute and return `n * (n-1) * ... * 1` using a loop.

3. `max_of_two(a, b)`:
   - Returns whichever is greater. If equal, return either.

### Sample Run
```python
print(MathUtil.is_prime(7))     # True
print(MathUtil.is_prime(10))    # False
print(MathUtil.is_prime(1))     # False

print(MathUtil.factorial(5))    # 120
print(MathUtil.factorial(0))    # 1
print(MathUtil.factorial(-3))   # Factorial not defined for negative numbers

print(MathUtil.max_of_two(10, 25))   # 25
print(MathUtil.max_of_two(7, 7))     # 7
```
