# Practice Problems: Classes and Objects

Learn the very basics: how to create a class, give it attributes, and define methods that work with those attributes.

> **Key idea:** A *class* is like a blueprint. An *object* is something built from that blueprint. Attributes store data about the object. Methods are functions that belong to the object and can use its data.

---

## Problem 1 — Student Report Card

### Problem Statement
A high school teacher needs a digital grading helper to manage student performance at the end of the academic term. For each student, the system must store their identification details (full name and roll number) alongside their exam marks in three subjects: Mathematics, Science, and English. 

The teacher requires automated calculations for the student's average marks across the three subjects and an evaluation of their letter grade based on standard academic thresholds (A for 90+, B for 80+, C for 70+, D for 60+, and F for below 60). In addition, the system must produce a formatted, single-line progress summary displaying the student's roll number, name, calculated average, and letter grade for parent-teacher meetings.

### What You'll Learn
- How to define a class and initialize object state with `__init__`
- How to store data as instance attributes using `self`
- How to write instance methods that read and compute values from attributes

### Requirements & Specifications
Create a `Student` class:

1. **Constructor (`__init__`)**:
   - Parameters: `name`, `roll_no`, `math_marks`, `science_marks`, `english_marks`
   - Store each as an attribute using `self`

2. **Methods**:
   - `calculate_average()`: Returns the average of the three subject marks.
     - Formula: `(math_marks + science_marks + english_marks) / 3`
   - `get_grade()`: Returns a letter grade based on the average:
     - Average >= 90 → `"A"`
     - Average >= 80 → `"B"`
     - Average >= 70 → `"C"`
     - Average >= 60 → `"D"`
     - Below 60 → `"F"`
   - `display_report()`: Prints a summary like:
     ```
     Roll No: 101 | Name: Rahul Sharma | Average: 86.33 | Grade: B
     ```

### Sample Run
```python
s1 = Student("Rahul Sharma", 101, 88, 92, 79)

print(s1.calculate_average())  # 86.33333...
print(s1.get_grade())          # B
s1.display_report()
# Roll No: 101 | Name: Rahul Sharma | Average: 86.33 | Grade: B
```

---

## Problem 2 — Bookstore Inventory

### Problem Statement
A local independent bookstore manages a catalog of physical books and wants a lightweight inventory tracking system. Each book in the catalog has a title, an author, a retail price, and the current quantity available in stock.

The bookstore manager frequently runs promotional campaigns where a percentage discount is applied to the book's price, with validation to reject invalid discount percentages. When a customer purchases copies of a book, the system must verify whether adequate inventory exists before fulfilling the sale. If stock is sufficient, the inventory is decremented and the sale succeeds; if stock is insufficient, the sale is declined with an informative message. The manager also needs quick queries to check stock availability and inspect a clean, human-readable summary of book details.

### What You'll Learn
- Defining methods that modify attribute values (state mutation)
- Implementing input validation and conditional logic (`if/else`) within methods
- Designing methods with meaningful return values (e.g., boolean flags for success/failure)

### Requirements & Specifications
Create a `Book` class:

1. **Constructor (`__init__`)**:
   - Parameters: `title`, `author`, `price`, `stock`

2. **Methods**:
   - `apply_discount(percentage)`:
     - Reduces `price` by the given percentage.
     - Example: if price is 100 and percentage is 20, new price = 80.
     - If percentage is not between 1 and 100, print `"Invalid discount"` and don't change the price.
   - `is_in_stock()`: Returns `True` if there's at least 1 copy, `False` otherwise.
   - `sell(quantity)`:
     - If `quantity` is available in stock, reduce `stock` by that amount and return `True`.
     - If not enough stock, print `"Not enough stock"` and return `False`.
   - `get_details()`: Returns a string like:
     ```
     'Clean Code' by Robert C. Martin - $36.00 (Stock: 2 copies)
     ```

### Sample Run
```python
b = Book("Clean Code", "Robert C. Martin", 45.0, 5)

print(b.get_details())   # 'Clean Code' by Robert C. Martin - $45.00 (Stock: 5 copies)
b.apply_discount(20)
print(b.price)           # 36.0
print(b.sell(3))         # True
print(b.sell(5))         # Not enough stock → False
print(b.is_in_stock())   # True (2 copies left)
```

---

## Problem 3 — Smartphone Storage Tracker

### Problem Statement
Modern smartphones have finite internal storage shared across the operating system, media files, and installed applications. Users frequently attempt to download new apps or clean up old ones to free up space.

You are tasked with building a storage tracker for a mobile device. The system must monitor total storage capacity and currently used storage in gigabytes (GB). Before installing any new application, the tracker must compute the available free space and determine whether the incoming app fits. If space permits, the application is installed and storage usage increases; otherwise, the installation is rejected. When an application is deleted, the system releases the corresponding storage. Users can also view an overview displaying the device's brand, model, and current storage utilization.

### What You'll Learn
- Methods calling other helper methods on the same object (`self.some_method()`)
- Computing derived values dynamically from existing attributes without duplicating state
- Simulating resource allocation and deallocation through object methods

### Requirements & Specifications
Create a `Mobile` class:

1. **Constructor (`__init__`)**:
   - Parameters: `brand`, `model`, `total_storage`, `used_storage`
   - (Storage values are in GB as floats)

2. **Methods**:
   - `get_free_storage()`: Returns `total_storage - used_storage`.
   - `install_app(app_name, app_size)`:
     - If `app_size` fits in the free storage, add it to `used_storage`, print `"Installed <app_name>"`, and return `True`.
     - Otherwise, print `"Not enough storage for <app_name>"` and return `False`.
   - `uninstall_app(app_name, app_size)`:
     - Reduce `used_storage` by `app_size`.
     - Print `"Uninstalled <app_name>. Freed <app_size> GB"`.
   - `display_specs()`: Prints a summary like:
     ```
     Google Pixel 8 | Storage: 35.0/128.0 GB used
     ```

### Sample Run
```python
m = Mobile("Google", "Pixel 8", 128.0, 30.0)

print(m.get_free_storage())           # 98.0
m.install_app("PhotoEditor", 5.0)     # Installed PhotoEditor
m.install_app("HugeGame", 100.0)      # Not enough storage for HugeGame
m.display_specs()                     # Google Pixel 8 | Storage: 35.0/128.0 GB used
```
