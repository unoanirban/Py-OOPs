"""
## Problem 1 — Animals

### What you'll learn
- How to define a base class and a subclass
- How the subclass automatically gets the parent's methods
- Adding new methods specific to the subclass

### Requirements

Base class Animal:
   __init__(self, name, age)
   eat(food): Prints "<name> is eating <food>."
   sleep(): Prints "<name> is sleeping."
   get_info(): Returns "<name>, Age: <age>"

Subclass Dog(Animal):
   __init__(self, name, age, breed)
   Call super().__init__(name, age) to reuse Animal's constructor.
   bark(): Prints "<name> says: Woof!"
   fetch(item): Prints "<name> fetched the <item>!"

Subclass Cat(Animal):
   __init__(self, name, age, is_indoor)
   Call super().__init__(name, age)
   purr(): Prints "<name> is purring."
   meow(): Prints "<name> says: Meow!"

### Sample Run
dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.get_info())   # Buddy, Age: 3    (inherited from Animal!)
dog.eat("kibble")       # Buddy is eating kibble.
dog.bark()              # Buddy says: Woof!

cat = Cat("Luna", 2, is_indoor=True)
cat.eat("fish")         # Luna is eating fish.
cat.purr()              # Luna is purring.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

