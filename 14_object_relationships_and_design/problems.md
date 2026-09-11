# Practice Problems: Object Relationships and Design

Apply everything you've learned to design multi-class systems where objects collaborate and keep each other's state in sync.

> **Key idea:** Real programs are made of many objects talking to each other. A `Library` doesn't just have a list of books — it manages the relationship *between* books and members. When a book is borrowed, BOTH the book's status AND the member's list must update together.

---

## Problem 1 — Library Book Borrowing System

### Problem Statement
A municipal public library requires an automated circulation system to manage its physical book collection and patron memberships. The system must track each book's catalog metadata (ISBN, title, author) and real-time availability status, as well as each member's borrowing activity up to an allowable quota (maximum 3 books by default).

When a patron requests to borrow a book, the `Library` acts as the central coordinator: it must verify that both the member and book exist, ensure the book is currently on the shelf, and verify that the patron has not exceeded their borrowing allowance. Upon loan approval, the system must synchronize state across both entities simultaneously—flagging the book as borrowed, recording the borrower's ID, and appending the book to the patron's active loans. Similarly, when a book is returned, the library must verify the patron holds the book, restore its available status, clear borrower references, and remove the title from the patron's account.

### What You'll Learn
- Designing multi-class architectures where an orchestrator (`Library`) coordinates interactions between domain entities (`Book`, `Member`)
- Maintaining two-way referential integrity and synchronized state across collaborating objects
- Enforcing borrowing quotas, validation guards, and error reporting in complex business workflows

### Requirements & Specifications

1. **Class `Book`**:
   - Constructor: `__init__(self, isbn, title, author)`
   - Attributes: `self.is_available = True`, `self.borrowed_by = None`
   - Method `get_info()`: Returns `"[<isbn>] '<title>' by <author> | {'Available' if is_available else 'Borrowed'}"`

2. **Class `Member`**:
   - Constructor: `__init__(self, member_id, name, max_limit=3)`
   - Attributes: `self.borrowed_books = []`
   - Method `can_borrow()`: Returns `True` if `len(borrowed_books) < max_limit`.
   - Method `get_profile()`: Returns `"<name> (ID: <member_id>) | Borrowed: <count> books"`

3. **Class `Library`**:
   - Constructor: `__init__(self, name)`
   - Attributes: `self.books = {}` (isbn → Book), `self.members = {}` (member_id → Member)
   - Methods:
     - `add_book(book)`: Adds to `self.books`.
     - `register_member(member)`: Adds to `self.members`.
     - `borrow_book(member_id, isbn)`:
       - If member or book not found, print error and return `False`.
       - If book not available, print `"Book not available."` and return `False`.
       - If member can't borrow more, print `"Borrow limit reached."` and return `False`.
       - Update: `book.is_available = False`, `book.borrowed_by = member_id`, append book to member's list.
       - Print confirmation. Return `True`.
     - `return_book(member_id, isbn)`:
       - Find book in member's `borrowed_books`.
       - If not found, print `"This member doesn't have this book."` and return `False`.
       - Restore: `book.is_available = True`, `book.borrowed_by = None`, remove from member's list.
       - Print confirmation. Return `True`.

### Sample Run
```python
lib = Library("City Library")

b1 = Book("ISBN001", "Python Tricks", "Dan Bader")
b2 = Book("ISBN002", "Clean Code", "Robert Martin")
m1 = Member("M001", "Rahul")

lib.add_book(b1)
lib.add_book(b2)
lib.register_member(m1)

lib.borrow_book("M001", "ISBN001")   # Rahul borrowed 'Python Tricks'
print(m1.get_profile())             # Rahul (ID: M001) | Borrowed: 1 books
print(b1.get_info())                # [ISBN001] 'Python Tricks' by Dan Bader | Borrowed

lib.return_book("M001", "ISBN001")  # Rahul returned 'Python Tricks'
print(b1.get_info())                # [ISBN001] 'Python Tricks' by Dan Bader | Available
```

---

## Problem 2 — School Enrollment System

### Problem Statement
An academic registrar platform manages course registration across university departments. Courses have strict maximum seat capacities to avoid overcrowding, and each course is assigned a qualified faculty instructor (`Teacher`).

When a `Student` attempts to register for a `Course`, the course object must perform critical admission checks: verifying whether the course is already at full capacity and ensuring the student has not already registered (preventing duplicate enrollments). If all checks pass, the course adds the student to its official enrollment roster, and the student's personal schedule (`enrolled_courses`) records the newly added course code. The system must also provide roster inspection methods to print numbered attendee listings.

### What You'll Learn
- Coordinating bi-directional relationships between courses and participating students
- Enforcing structural capacity constraints and duplicate-prevention guards
- Assigning instructor associations to academic course containers

### Requirements & Specifications

1. **Class `Teacher`**:
   - Constructor: `__init__(self, name, subject)`

2. **Class `Student`**:
   - Constructor: `__init__(self, student_id, name)`
   - Attributes: `self.enrolled_courses = []`

3. **Class `Course`**:
   - Constructor: `__init__(self, code, title, max_capacity)`
   - Attributes: `self.students = []`, `self.instructor = None`
   - Methods:
     - `assign_instructor(teacher)`: Sets `self.instructor = teacher`. Prints `"<teacher.name> assigned to <title>."`
     - `enroll_student(student)`:
       - If full, print `"Course <code> is full."` and return `False`.
       - If already enrolled, print `"Already enrolled."` and return `False`.
       - Add student to `self.students`, add `self.code` to `student.enrolled_courses`. Return `True`.
     - `get_roster()`: Prints all enrolled students, numbered.

### Sample Run
```python
t1 = Teacher("Dr. Priya", "Data Structures")
s1 = Student("S001", "Aarav")
s2 = Student("S002", "Diya")
course = Course("CS201", "Data Structures", max_capacity=2)

course.assign_instructor(t1)    # Dr. Priya assigned to Data Structures.
course.enroll_student(s1)       # Aarav enrolled in CS201
course.enroll_student(s2)       # Diya enrolled in CS201
course.enroll_student(s1)       # Already enrolled.
course.get_roster()
# 1. Aarav (S001)
# 2. Diya (S002)

print(s1.enrolled_courses)      # ['CS201']
```

---

## Problem 3 — Shopping Cart & Order System

### Problem Statement
An online shopping application processes customer orders from product selection to payment checkout. Products in the store catalog maintain real-time physical inventory counts. Customers browse items and stage them in a shopping `Cart`, which aggregates selected items, tracks quantities, and computes total order sums.

When adding merchandise to a cart, the system must verify that adequate warehouse stock exists. When the customer executes `checkout()`, the system converts the temporary cart contents into an immutable, finalized order record, systematically deducts purchased quantities from warehouse stock levels, appends the order to the customer's purchase history, and clears the cart for future shopping sessions.

### What You'll Learn
- Orchestrating a full commercial workflow across `Product`, `Cart`, and `Customer` objects
- Managing multi-stage state transitions (from in-cart reservation to finalized order checkout)
- Decrementing inventory levels and preserving transactional consistency across composite entities

### Requirements & Specifications

1. **Class `Product`**:
   - Constructor: `__init__(self, product_id, name, price, stock)`
   - Method `get_info()`: Returns `"<name> | $<price> | Stock: <stock>"`
   - Method `reduce_stock(qty)`:
     - If `qty > stock`, print `"Not enough stock."` and return `False`.
     - Else reduce `stock` by `qty` and return `True`.

2. **Class `Cart`**:
   - Constructor: `__init__(self, customer_name)`
   - Attributes: `self.items = {}` (product → quantity)
   - Methods:
     - `add_item(product, quantity)`: Check stock, then add.
     - `get_total()`: Returns sum of `product.price * quantity` for all items.
     - `is_empty()`: Returns `True` if no items.
     - `show_items()`: Prints all items with quantities and prices.

3. **Class `Customer`**:
   - Constructor: `__init__(self, name)`
   - Attributes: `self.cart = Cart(name)`, `self.orders = []`
   - Method `checkout()`:
     - If cart is empty, print `"Cart is empty."` and return `None`.
     - Reduce stock for all items in cart.
     - Create an order dict `{"items": [...], "total": ...}`.
     - Append to `self.orders`, clear the cart (`self.cart.items = {}`).
     - Print `"Order placed! Total: $<total>"`. Return the order dict.

### Sample Run
```python
p1 = Product("P01", "Python Book", 500, 10)
p2 = Product("P02", "Mechanical Keyboard", 3000, 5)

customer = Customer("Rahul")
customer.cart.add_item(p1, 2)
customer.cart.add_item(p2, 1)
customer.cart.show_items()
# Python Book x2 — $1000
# Mechanical Keyboard x1 — $3000

order = customer.checkout()   # Order placed! Total: $4000
print(p1.stock)               # 8 (reduced from 10)
print(customer.cart.is_empty())  # True
```
