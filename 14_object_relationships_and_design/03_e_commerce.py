"""
## Problem 3 — Shopping Cart & Order System

### Requirements

Class Product:
   __init__(self, product_id, name, price, stock)
   get_info(): Returns "<name> | $<price> | Stock: <stock>"
   reduce_stock(qty): Reduce stock if available, else print error.

Class Cart:
   __init__(self, customer_name)
   self.items = {}  (product → quantity)
   add_item(product, quantity): Check stock first.
   get_total(): Sum of price * qty.
   is_empty(): True if no items.
   show_items(): Prints each item with totals.

Class Customer:
   __init__(self, name)
   self.cart = Cart(name)
   self.orders = []
   checkout(): Place order, reduce stock, clear cart.

### Sample Run (see problems.md for full sample)

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

