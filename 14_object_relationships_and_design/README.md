# Module 14 — Object Relationships and Software Design

In previous modules, you learned individual OOP tools: classes, inheritance, encapsulation, polymorphism, and composition.

In this module, you will learn how to connect these pieces together to design **multi-class systems** where multiple objects collaborate harmoniously.

---

## 1. Concept Overview: Ecosystems of Objects

Real-world applications are never written as a single giant class. Instead, they are built as an **ecosystem of cooperating objects**:
- In an e-commerce store, a `Customer` adds a `Product` to a `Cart`, checks out an `Order`, and pays via a `PaymentGateway`.
- In a library, a `Member` searches a `Catalog`, borrows a `Book`, and receives a `Receipt`.

To build clean, maintainable systems, you must choose the right relationship between your classes.

```
+---------------------------------------------------------------------------------+
|                               OBJECT RELATIONSHIPS                              |
+---------------------------------------------------------------------------------+
| 1. Dependency ("Uses-A")                                                        |
|    - An object temporarily interacts with another (passed as a parameter).      |
|    - Example: printer.print_document(doc)                                       |
+---------------------------------------------------------------------------------+
| 2. Aggregation ("Has-A" — Weak Lifecycle)                                       |
|    - A container holds references to independent objects created outside.      |
|    - Example: Library has Books (books can exist before/after the library).     |
+---------------------------------------------------------------------------------+
| 3. Composition ("Has-A" — Strong Lifecycle)                                     |
|    - A container strictly creates and owns its parts; parts die with container. |
|    - Example: Order owns OrderItems (an item cannot exist without an order).    |
+---------------------------------------------------------------------------------+
| 4. Inheritance ("Is-A")                                                         |
|    - Specialization and taxonomy.                                               |
|    - Example: PremiumMember is a Member.                                        |
+---------------------------------------------------------------------------------+
```

---

## 2. Bidirectional Consistency: The Single Coordinator Pattern

A common challenge in multi-object systems is keeping related objects in sync.

For example, when a `Member` borrows a `Book`:
1. The `book.is_available` flag must become `False`.
2. The `book` must be added to `member.borrowed_books`.

### The Anti-Pattern (Fragile Code):
```python
# FRAGILE: External code manually updates both objects
book.is_available = False
member.borrowed_books.append(book)
# If a developer forgets one line, your system state is corrupted!
```

### The Clean Solution: The Coordinator Pattern
Always encapsulate the transaction inside a single coordinating method (e.g., inside `Library`):

```python
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.is_available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    # THE COORDINATOR METHOD:
    def borrow_book(self, member, isbn):
        """Coordinates borrowing safely in one atomic place."""
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_available:
                    print(f"'{book.title}' is currently checked out.")
                    return False
                
                # Atomically update both objects together!
                book.is_available = False
                member.borrowed_books.append(book)
                print(f"Success: {member.name} borrowed '{book.title}'.")
                return True
                
        print(f"Book with ISBN {isbn} not found.")
        return False
```

Now, outside callers simply call `library.borrow_book(member, "123-456")`. The internal consistency is guaranteed!

---

## 3. Core Design Principles

When designing multi-class applications, follow these key principles:

### A. Single Responsibility Principle (SRP)
Every class should have **one, and only one, responsibility**:
- `Book` manages book data.
- `Member` manages member profile and personal loans.
- `Library` manages the collection and circulation transactions.
- Do not make a single class handle UI, database, business logic, and file exports all at once!

### B. Avoid the "God Object" Anti-Pattern
A **God Object** is a colossal class that knows everything, controls everything, and does everything (thousands of lines), while all other classes are reduced to dumb data holders with no methods.
- **Remedy**: Push logic down into the classes that own the data! If an action is about a `Book`, put that method inside `Book`.

---

## 4. Step-by-Step Design Workflow

Before writing code for a multi-object project:
1. **Identify the Nouns**:
   Read the problem requirements and list the nouns. These are usually your **Classes** (`Book`, `Author`, `Catalog`).
2. **Identify the Adjectives & State**:
   What information does each entity need to remember? These are your **Attributes** (`price`, `is_available`, `email`).
3. **Identify the Verbs & Actions**:
   What can each entity do? These are your **Methods** (`borrow()`, `calculate_fine()`, `refund()`).
4. **Determine the Relationships**:
   Which class contains which? ("Has-A" -> Composition/Aggregation). Which class specializes another? ("Is-A" -> Inheritance).

---

## 5. Common Beginner Pitfalls

### Pitfall 1: Tight Coupling via Hardcoded Concrete Classes
If Class A directly imports and instantiates 10 specific other classes, you cannot easily test or modify Class A. Prefer passing dependencies into `__init__` or methods as arguments.

---

### Pitfall 2: Desynchronized Collections
If `member.borrowed_books` has 3 books, but `book.is_available` is still `True`, your data model is desynchronized. Always update both sides of a relationship inside a single coordinator method.

---

## 6. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] What is the difference between Dependency ("Uses-A") and Aggregation ("Has-A")?
- [ ] What is the Single Coordinator Pattern and why is it safer than manual attribute updates?
- [ ] What is the Single Responsibility Principle?
- [ ] What is a "God Object" and why should you avoid it?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice designing connected, multi-class systems!
