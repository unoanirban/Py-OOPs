"""
## Problem 3 — Exploring MRO (Diamond Inheritance)

### What you'll learn
- Python's Method Resolution Order (MRO)
- How super() follows the MRO chain in diamond inheritance

### Requirements

Class A:
   greet(): Prints "Hello from A"
   who_am_i(): Returns "A"

Class B(A):
   greet(): Prints "Hello from B", then calls super().greet()
   who_am_i(): Returns "B"

Class C(A):
   greet(): Prints "Hello from C", then calls super().greet()
   who_am_i(): Returns "C"

Class D(B, C):
   Inherits from both — no new methods needed.

### Sample Run
d = D()
d.greet()
# Hello from B
# Hello from C
# Hello from A

print(d.who_am_i())    # B  (first in MRO after D)
print(D.__mro__)       # D → B → C → A → object

### Tip
The MRO determines the order Python looks for a method.
D's MRO is: D → B → C → A → object
super() in B doesn't go to A — it goes to the NEXT in MRO, which is C!

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

