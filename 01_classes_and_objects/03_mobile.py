"""
## Problem 3 — Smartphone Storage Tracker

### What you'll learn
- Methods calling other methods (self.some_method())
- Computing derived values from stored attributes

### Context
Your phone has limited storage. This class tracks how much storage
is used and warns you when there isn't enough space to install a new app.

### Requirements
Create a Mobile class:

1. Constructor (__init__):
   - Parameters: brand, model, total_storage, used_storage
   - (Storage values are in GB as floats)

2. Methods:
   - get_free_storage(): Returns total_storage - used_storage.

   - install_app(app_name, app_size):
       If app_size fits in the free storage, add it to used_storage,
       print "Installed <app_name>", and return True.
       Otherwise, print "Not enough storage for <app_name>" and return False.

   - uninstall_app(app_name, app_size):
       Reduce used_storage by app_size.
       Print "Uninstalled <app_name>. Freed <app_size> GB"

   - display_specs(): Prints a summary like:
       Google Pixel 8 | Storage: 35.0/128.0 GB used

### Sample Run
m = Mobile("Google", "Pixel 8", 128.0, 30.0)

print(m.get_free_storage())           # 98.0
m.install_app("PhotoEditor", 5.0)     # Installed PhotoEditor
m.install_app("HugeGame", 100.0)      # Not enough storage for HugeGame
m.display_specs()                     # Google Pixel 8 | Storage: 35.0/128.0 GB used

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

