"""
## Project 1 — Enterprise Library Circulation & Fine Management

### System Specifications
1. **Class `Book`**:
   - `__init__(isbn: str, title: str, author: str, total_copies: int = 1)`
   - Attributes: `available_copies: int` (initialized to `total_copies`).
   - Properties / Validations: `total_copies >= 1`, `0 <= available_copies <= total_copies`.
2. **Class `Member`**:
   - `__init__(member_id: str, name: str, max_borrow_limit: int = 3)`
   - Attributes:
     - `borrowed_isbns: list[str] = []`
     - `outstanding_fines: float = 0.0`
   - Methods:
     - `can_borrow() -> bool`: Returns `True` if `len(borrowed_isbns) < max_borrow_limit` and `outstanding_fines == 0.0`.
     - `pay_fine(amount: float) -> float`: Deducts from fine, returns remaining fine.
3. **Class `Library`**:
   - `__init__(name: str)`
   - Catalog: `books: dict[str, Book]`
   - Registry: `members: dict[str, Member]`
   - Methods:
     - `add_book(book: Book) -> None`
     - `register_member(member: Member) -> None`
     - `search(query: str) -> list[Book]`: Case-insensitive search across title and author.
     - `borrow_book(member_id: str, isbn: str) -> bool`:
       - Verifies member and book exist.
       - Checks `member.can_borrow()` and `book.available_copies > 0`.
       - Deducts `book.available_copies`, adds ISBN to member's borrowed list.
     - `return_book(member_id: str, isbn: str, days_overdue: int = 0) -> bool`:
       - If `days_overdue > 0`, assesses fine of `$0.50` per day to member.
       - Restores `book.available_copies`, removes ISBN from member list.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:
