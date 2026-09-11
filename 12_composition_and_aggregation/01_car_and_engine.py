"""
## Problem 1 — Car and Engine (Composition)

### Requirements

Class Engine:
   __init__(self, horsepower, fuel_type)
   start(): Prints "Engine started. <horsepower>hp <fuel_type> engine roaring!"
   stop(): Prints "Engine stopped."
   get_specs(): Returns "<horsepower>hp <fuel_type> engine"

Class Car:
   __init__(self, make, model, year, horsepower, fuel_type)
       Create the Engine inside __init__: self.engine = Engine(horsepower, fuel_type)
   start_car(): Prints starting message, then calls self.engine.start()
   stop_car(): Calls self.engine.stop(), then prints parking message
   get_info(): Returns "<year> <make> <model> | <engine.get_specs()>"

### Sample Run
car = Car("Toyota", "Camry", 2023, 203, "Petrol")
car.start_car()
# Starting Toyota Camry...
# Engine started. 203hp Petrol engine roaring!
print(car.get_info())   # 2023 Toyota Camry | 203hp Petrol engine
car.stop_car()
# Engine stopped.
# Toyota Camry parked.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

