"""
## Problem 1 — Temperature Converter

### What you'll learn
- Defining @staticmethod methods
- Calling static methods without creating an object

### Context
A weather app needs to convert temperatures between Celsius, Fahrenheit,
and Kelvin. These conversions don't depend on any object, so static methods
are the perfect fit.

### Requirements
Create a TemperatureConverter class with these static methods:

1. celsius_to_fahrenheit(c):  Formula: (c * 9/5) + 32
2. fahrenheit_to_celsius(f):  Formula: (f - 32) * 5/9
3. celsius_to_kelvin(c):      Formula: c + 273.15
4. kelvin_to_celsius(k):      Formula: k - 273.15

### Sample Run
print(TemperatureConverter.celsius_to_fahrenheit(100))   # 212.0
print(TemperatureConverter.fahrenheit_to_celsius(32))    # 0.0
print(TemperatureConverter.celsius_to_kelvin(25))        # 298.15
print(TemperatureConverter.kelvin_to_celsius(0))         # -273.15

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

