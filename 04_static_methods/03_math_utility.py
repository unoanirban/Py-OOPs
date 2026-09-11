"""
## Problem 3 — Math Utility

### What you'll learn
- More static methods for utility calculations
- Using loops inside static methods

### Context
A math utility class for a school app: check if a number is prime,
compute factorials, and find the larger of two numbers.

### Requirements
Create a MathUtil class with these static methods:

1. is_prime(n):
   - Returns False if n <= 1.
   - Loop from 2 to n-1. If n % i == 0 for any i, it's not prime.
   - Otherwise return True.

2. factorial(n):
   - Returns 1 if n == 0.
   - If n < 0, print "Factorial not defined for negative numbers" and return None.
   - Otherwise compute n * (n-1) * ... * 1 using a loop.

3. max_of_two(a, b):
   - Returns whichever is greater. If equal, return either.

### Sample Run
print(MathUtil.is_prime(7))          # True
print(MathUtil.is_prime(10))         # False
print(MathUtil.factorial(5))         # 120
print(MathUtil.factorial(0))         # 1
print(MathUtil.factorial(-3))        # Factorial not defined for negative numbers
print(MathUtil.max_of_two(10, 25))   # 25

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

