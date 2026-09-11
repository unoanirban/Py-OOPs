"""
## Problem 2 — Computer and Components (Composition)

### Requirements

Class CPU:
   __init__(self, brand, cores, speed_ghz)
   get_info(): Returns "<brand> CPU: <cores> cores @ <speed_ghz>GHz"

Class RAM:
   __init__(self, size_gb, speed_mhz)
   get_info(): Returns "<size_gb>GB RAM @ <speed_mhz>MHz"

Class Storage:
   __init__(self, size_gb, storage_type)
   get_info(): Returns "<size_gb>GB <storage_type>"

Class Computer:
   __init__(self, brand, cpu, ram, storage)
       cpu, ram, storage are already-created objects passed in.
   get_full_specs(): Prints all specs.

### Sample Run
cpu = CPU("Intel", 8, 3.6)
ram = RAM(16, 3200)
storage = Storage(512, "SSD")
pc = Computer("Dell", cpu, ram, storage)
pc.get_full_specs()
# Brand: Dell
# CPU: Intel CPU: 8 cores @ 3.6GHz
# RAM: 16GB RAM @ 3200MHz
# Storage: 512GB SSD

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

