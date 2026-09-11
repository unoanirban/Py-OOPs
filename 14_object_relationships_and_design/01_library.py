"""
## Problem 1 — Library Book Borrowing System

### Requirements

Class Book:
   __init__(self, isbn, title, author)
   self.is_available = True, self.borrowed_by = None
   get_info(): Returns "[<isbn>] '<title>' by <author> | <status>"

Class Member:
   __init__(self, member_id, name, max_limit=3)
   self.borrowed_books = []
   can_borrow(): Returns True if borrowed_books count < max_limit
   get_profile(): Returns "<name> (ID: <member_id>) | Borrowed: <count> books"

Class Library:
   __init__(self, name)
   self.books = {}, self.members = {}
   add_book(book), register_member(member)
   borrow_book(member_id, isbn): Validate, update both book and member.
   return_book(member_id, isbn): Restore availability, update member list.

### Sample Run (see problems.md for full sample)

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

