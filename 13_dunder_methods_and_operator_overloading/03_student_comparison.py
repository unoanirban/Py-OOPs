"""
## Problem 3 — Shopping Cart with __len__, __str__, __contains__

### Requirements

Class ShoppingCart:
   __init__(self, owner)
       self.items = {}  (item_name → quantity)
   add_item(name, quantity): Add/increase quantity.
   remove_item(name): Remove item or print "Item not found."
   __len__: Returns total quantity across all items.
   __contains__(item_name): Returns True if item_name is in self.items.
   __str__: Returns "Cart (<owner>): <item> x<qty>, ... | Total items: <total>"

### Sample Run
cart = ShoppingCart("Rahul")
cart.add_item("Apple", 2)
cart.add_item("Banana", 3)
cart.add_item("Milk", 1)

print(len(cart))              # 6
print("Apple" in cart)        # True
print("Juice" in cart)        # False
print(cart)
# Cart (Rahul): Apple x2, Banana x3, Milk x1 | Total items: 6

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

