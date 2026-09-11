"""
## Problem 1 — Animal Sounds

### What you'll learn
- Overriding a method from the parent class
- The subclass's method completely replaces the parent's version

### Requirements

Base class Animal:
   __init__(self, name)
   make_sound(): Prints "<name> makes a sound."
   describe(): Prints "I am an animal named <name>."

Subclass Dog(Animal):
   Overrides make_sound(): Prints "<name> says: Woof! Woof!"

Subclass Cat(Animal):
   Overrides make_sound(): Prints "<name> says: Meow!"

Subclass Cow(Animal):
   Overrides make_sound(): Prints "<name> says: Moo!"

### Sample Run
a = Animal("Generic Animal")
a.make_sound()    # Generic Animal makes a sound.
a.describe()      # I am an animal named Generic Animal.

d = Dog("Buddy")
d.make_sound()    # Buddy says: Woof! Woof!
d.describe()      # I am an animal named Buddy.  (inherited, not overridden)

c = Cat("Luna")
c.make_sound()    # Luna says: Meow!

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

