"""
## Problem 3 — Product with Automatic Price Calculation

### What you'll learn
- Multiple properties in one class
- A read-only property that computes from other properties

### Context
An online store has products with a base price and a tax rate.
The final price is always calculated automatically.

### Requirements
Create a Product class:

1. Constructor (__init__):
   - Parameters: name, price, tax_rate (default = 0.1 for 10%)

2. Property price:
   - Getter: returns self._price
   - Setter: if value < 0, print "Price cannot be negative." and don't update.
             Otherwise set self._price = value.

3. Property tax_rate:
   - Getter: returns self._tax_rate
   - Setter: if value < 0 or value > 1, print "Tax rate must be between 0 and 1."
             and don't update. Otherwise set self._tax_rate = value.

4. Property final_price (read-only — no setter):
   - Returns self._price * (1 + self._tax_rate)

5. Method apply_discount(percent):
   - If percent < 0 or percent > 100, print "Invalid discount." and return.
   - Set self.price = self._price * (1 - percent / 100)

### Sample Run
prod = Product("Headphones", 1000, 0.18)
print(prod.price)        # 1000
print(prod.final_price)  # 1180.0

prod.apply_discount(10)
print(prod.price)        # 900.0
print(prod.final_price)  # 1062.0

prod.price = -50         # Price cannot be negative.
print(prod.price)        # 900.0 (unchanged)

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

