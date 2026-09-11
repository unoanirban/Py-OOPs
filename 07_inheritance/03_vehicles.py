"""
## Problem 3 — Vehicles

### What you'll learn
- Multiple subclasses with their own specific attributes and behaviors

### Requirements

Base class Vehicle:
   __init__(self, make, model, year)
   get_description(): Returns "<year> <make> <model>"

Subclass Truck(Vehicle):
   __init__(self, make, model, year, payload_capacity)
   self.current_load = 0
   load_cargo(weight): Add if fits; else print "Overload! Cannot carry that much."
   unload(): Sets current_load to 0, prints "Cargo unloaded."

Subclass ElectricCar(Vehicle):
   __init__(self, make, model, year, battery_capacity)
   self.battery_level = 0
   charge(kwh): Add kwh up to battery_capacity. Print actual amount charged.
   drive(km, efficiency): If enough battery, subtract used kWh. Else print "Not enough battery."

### Sample Run
truck = Truck("Tata", "Ace", 2021, 1000)
print(truck.get_description())   # 2021 Tata Ace
truck.load_cargo(600)            # Loaded 600 kg.
truck.load_cargo(600)            # Overload! Cannot carry that much.

ev = ElectricCar("Tesla", "Model 3", 2023, 75)
ev.charge(50)       # Charged 50 kWh.
ev.drive(200, 6)    # Drove 200 km.
ev.drive(300, 6)    # Not enough battery.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

