# Solutions: 14 — Object Relationships and Design

## Problem 1 — Library Book Borrowing System

```python
class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_available = True
        self.borrowed_by = None

    def get_info(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.isbn}] '{self.title}' by {self.author} | {status}"


class Member:
    def __init__(self, member_id, name, max_limit=3):
        self.member_id = member_id
        self.name = name
        self.max_limit = max_limit
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_limit

    def get_profile(self):
        return f"{self.name} (ID: {self.member_id}) | Borrowed: {len(self.borrowed_books)} books"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            print("Member not found.")
            return False
        if isbn not in self.books:
            print("Book not found.")
            return False

        member = self.members[member_id]
        book = self.books[isbn]

        if not book.is_available:
            print("Book not available.")
            return False
        if not member.can_borrow():
            print("Borrow limit reached.")
            return False

        book.is_available = False
        book.borrowed_by = member_id
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed '{book.title}'.")
        return True

    def return_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)
        if not member or not book:
            print("Member or book not found.")
            return False

        if book not in member.borrowed_books:
            print("This member doesn't have this book.")
            return False

        book.is_available = True
        book.borrowed_by = None
        member.borrowed_books.remove(book)
        print(f"{member.name} returned '{book.title}'.")
        return True


# Try it out
lib = Library("City Library")

b1 = Book("ISBN001", "Python Tricks", "Dan Bader")
b2 = Book("ISBN002", "Clean Code", "Robert Martin")
m1 = Member("M001", "Rahul")

lib.add_book(b1)
lib.add_book(b2)
lib.register_member(m1)

lib.borrow_book("M001", "ISBN001")   # Rahul borrowed 'Python Tricks'.
print(m1.get_profile())             # Rahul (ID: M001) | Borrowed: 1 books
print(b1.get_info())                # [ISBN001] 'Python Tricks' by Dan Bader | Borrowed

lib.return_book("M001", "ISBN001")  # Rahul returned 'Python Tricks'.
print(b1.get_info())                # [ISBN001] 'Python Tricks' by Dan Bader | Available
```

---

## Problem 2 — School Enrollment System

```python
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []


class Course:
    def __init__(self, code, title, max_capacity):
        self.code = code
        self.title = title
        self.max_capacity = max_capacity
        self.students = []
        self.instructor = None

    def assign_instructor(self, teacher):
        self.instructor = teacher
        print(f"{teacher.name} assigned to {self.title}.")

    def enroll_student(self, student):
        if len(self.students) >= self.max_capacity:
            print(f"Course {self.code} is full.")
            return False
        if student in self.students:
            print("Already enrolled.")
            return False
        self.students.append(student)
        student.enrolled_courses.append(self.code)
        print(f"{student.name} enrolled in {self.code}.")
        return True

    def get_roster(self):
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student.name} ({student.student_id})")


# Try it out
t1 = Teacher("Dr. Priya", "Data Structures")
s1 = Student("S001", "Aarav")
s2 = Student("S002", "Diya")
course = Course("CS201", "Data Structures", max_capacity=2)

course.assign_instructor(t1)
course.enroll_student(s1)
course.enroll_student(s2)
course.enroll_student(s1)    # Already enrolled.
course.get_roster()
print(s1.enrolled_courses)   # ['CS201']
```

---

## Problem 3 — Shopping Cart & Order System

```python
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def get_info(self):
        return f"{self.name} | ${self.price} | Stock: {self.stock}"

    def reduce_stock(self, qty):
        if qty > self.stock:
            print(f"Not enough stock for {self.name}.")
            return False
        self.stock -= qty
        return True


class Cart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}

    def add_item(self, product, quantity):
        if quantity > product.stock:
            print(f"Not enough stock for {product.name}.")
            return False
        self.items[product] = self.items.get(product, 0) + quantity
        print(f"Added {product.name} x{quantity} to cart.")
        return True

    def get_total(self):
        return sum(p.price * qty for p, qty in self.items.items())

    def is_empty(self):
        return len(self.items) == 0

    def show_items(self):
        for product, qty in self.items.items():
            print(f"{product.name} x{qty} — ${product.price * qty}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart(name)
        self.orders = []

    def checkout(self):
        if self.cart.is_empty():
            print("Cart is empty.")
            return None

        total = self.cart.get_total()
        order_items = []
        for product, qty in self.cart.items.items():
            product.reduce_stock(qty)
            order_items.append({"name": product.name, "qty": qty, "price": product.price})

        order = {"items": order_items, "total": total}
        self.orders.append(order)
        self.cart.items = {}
        print(f"Order placed! Total: ${total}")
        return order


# Try it out
p1 = Product("P01", "Python Book", 500, 10)
p2 = Product("P02", "Mechanical Keyboard", 3000, 5)

customer = Customer("Rahul")
customer.cart.add_item(p1, 2)
customer.cart.add_item(p2, 1)
customer.cart.show_items()

order = customer.checkout()    # Order placed! Total: $4000
print(p1.stock)                # 8
print(customer.cart.is_empty()) # True
```
