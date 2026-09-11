"""
## Problem 1 — Car Fuel Tracker

### What you'll learn
- Using __init__ to set starting state
- Simple validation: check a condition and print an error if it fails
- State mutation: methods that update self.attribute

### Context
You're building a program to track a car's fuel level and how far it has
driven. When you drive, fuel gets used up. When you refuel, the tank fills back up.

### Requirements
Create a Car class:

1. Constructor (__init__):
   - Parameters: brand, model, fuel_capacity, fuel_efficiency
       fuel_capacity: how many liters the tank can hold (e.g., 50)
       fuel_efficiency: how many km you get per liter (e.g., 15)
   - Set fuel_level to fuel_capacity at the start (full tank)
   - Set odometer to 0 (no km driven yet)
   - If fuel_capacity <= 0 or fuel_efficiency <= 0, print "Invalid values"

2. Methods:
   - drive(distance_km):
       Calculate fuel needed: distance_km / fuel_efficiency
       If enough fuel: subtract fuel used, add distance to odometer, print confirmation.
       If not enough fuel: print "Not enough fuel to drive that far."

   - refuel(liters):
       Add liters to fuel_level, but don't go over fuel_capacity.
       Print how many liters were actually added.

   - get_status():
       Prints: Toyota Camry | Odometer: 300.0 km | Fuel: 30.0/50.0 L

### Sample Run
car = Car("Toyota", "Camry", 50, 15)
car.get_status()   # Toyota Camry | Odometer: 0.0 km | Fuel: 50/50 L
car.drive(300)     # Drove 300 km
car.get_status()   # Toyota Camry | Odometer: 300.0 km | Fuel: 30.0/50 L
car.drive(600)     # Not enough fuel to drive that far.
car.refuel(25)     # Added 20.0 L (tank is full)

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

