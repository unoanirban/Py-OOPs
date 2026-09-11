"""
## Problem 3 — Vehicle Abstract Base

### Requirements

Abstract base class Vehicle (inherits from ABC):
   __init__(self, make, model)
   self.mileage = 0
   @abstractmethod refuel(): Subclasses define how to refuel.
   @abstractmethod get_range(): Returns estimated range in km.
   Regular drive(km): Adds km to mileage, prints message.
   Regular get_info(): Returns "<make> <model> | Mileage: <mileage> km"

Class PetrolCar(Vehicle):
   __init__(self, make, model, tank_capacity, efficiency)
   self.fuel_level = 0
   refuel(): Fills tank, prints "Petrol tank full."
   get_range(): Returns fuel_level * efficiency

Class ElectricCar(Vehicle):
   __init__(self, make, model, battery_capacity, efficiency)
   self.battery_level = 0
   refuel(): Charges battery, prints "Battery fully charged."
   get_range(): Returns battery_level * efficiency

### Sample Run
petrol = PetrolCar("Honda", "City", 40, 18)
petrol.refuel()              # Petrol tank full.
print(petrol.get_range())    # 720
petrol.drive(200)            # Drove 200 km. Total mileage: 200 km.

ev = ElectricCar("Tesla", "Model 3", 75, 6)
ev.refuel()                  # Battery fully charged.
print(ev.get_range())        # 450

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

from abc import ABC, abstractmethod

# Write your solution here:

