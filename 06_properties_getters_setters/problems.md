# Practice Problems: Properties, Getters, and Setters

Learn to use Python's `@property` decorator to create **smart attributes** — ones that validate data when set and compute values automatically when read.

> **Key idea:** Without `@property`, you'd need `get_name()` and `set_name()` methods. With `@property`, you can write `person.name = "Rahul"` and Python secretly runs your validation code. It looks like a simple attribute assignment but has the power of a method behind it.

---

## Problem 1 — Employee Salary with Validation

### Problem Statement
A human resources management system maintains records of employee compensation. In payroll processing, an employee's salary must never be assigned a negative number. 

Traditional object-oriented languages often rely on verbose explicit getter and setter methods like `get_salary()` and `set_salary(val)`. Python provides a more elegant and idiomatic solution using the `@property` decorator, allowing attributes to be accessed and assigned using natural syntax (`emp.salary = 7000`) while executing validation logic under the hood. In this problem, you need to model an employee salary property where any assignment of a negative amount is caught, reported, and clamped to a safe default of 0.

### What You'll Learn
- Defining getter methods with `@property` and setter methods with `@<property_name>.setter`
- Routing initial constructor assignments through property setters for consistent validation
- Writing Pythonic, clean code that looks like direct attribute access while preserving data invariants

### Requirements & Specifications
Create an `Employee` class:

1. **Constructor (`__init__`)**:
   - Parameters: `name`, `salary`
   - **Do not** assign `self.salary = salary` directly. Instead, use `self.salary = salary` which will call the property setter automatically.

2. **Property `salary`**:
   - **Getter**: returns `self._salary`
   - **Setter**: if `value < 0`, print `"Salary cannot be negative."` and set `self._salary = 0`. Otherwise set `self._salary = value`.

3. **Method**:
   - `get_info()`: Returns `"<name> earns $<salary> per month"`

### Sample Run
```python
emp = Employee("Rahul", 5000)
print(emp.salary)         # 5000
print(emp.get_info())     # Rahul earns $5000 per month

emp.salary = 7000         # updates via setter
print(emp.salary)         # 7000

emp.salary = -500         # Salary cannot be negative.
print(emp.salary)         # 0 (fallback)
```

> **Notice:** `emp.salary = 7000` looks like a regular assignment, but it secretly calls the setter method with `value = 7000`.

---

## Problem 2 — Person with a Computed Full Name

### Problem Statement
A civil registry and identity verification system stores personal records. Each person has a separate first name and last name, as well as an age. 

Storing a concatenated "full name" as a static attribute alongside the first and last names leads to data synchronization problems: if an individual changes their first name, the stored full name becomes out of sync unless manually updated. Instead, full name should be exposed as a dynamic, read-only computed property that joins the current first and last names on demand. Additionally, human age requires strict validation to guard against negative numbers or biologically impossible values (e.g., above 120), rejecting invalid attempts without corrupting existing age values.

### What You'll Learn
- Creating read-only computed properties that dynamically reflect underlying state without storing redundant data
- Implementing range validation in property setters to protect boundary conditions
- Combining multiple attributes into synthetic properties

### Requirements & Specifications
Create a `Person` class:

1. **Constructor (`__init__`)**:
   - Parameters: `first_name`, `last_name`, `age`
   - Store each as `self.first_name`, `self.last_name`, `self._age`

2. **Property `full_name`** (read-only — no setter needed):
   - Getter: Returns `f"{self.first_name} {self.last_name}"`

3. **Property `age`**:
   - **Getter**: returns `self._age`
   - **Setter**: if `value < 0` or `value > 120`, print `"Invalid age."` and do nothing. Otherwise update `self._age`.

4. **Method**:
   - `get_info()`: Returns `"<full_name>, Age: <age>"`

### Sample Run
```python
p = Person("Rahul", "Dravid", 45)
print(p.full_name)    # Rahul Dravid
print(p.get_info())   # Rahul Dravid, Age: 45

p.age = 50
print(p.age)          # 50

p.age = -5            # Invalid age.
print(p.age)          # 50 (unchanged)

# full_name is computed — it always reflects current names
p.first_name = "Sachin"
print(p.full_name)    # Sachin Dravid
```

---

## Problem 3 — Product with Automatic Price Calculation

### Problem Statement
An e-commerce checkout engine handles pricing for retail products. Every product has a base price and an applicable tax rate (e.g., 18% tax). 

Allowing arbitrary manual assignment of a product's final checkout price introduces severe risks of calculation discrepancies and tax non-compliance. Instead, the final price must always be computed dynamically from the validated base price and tax rate. Both the base price (which cannot be negative) and the tax rate (which must strictly fall between 0.0 and 1.0) must be managed by validating property setters. The final price is exposed as a read-only property. Furthermore, when promotional discounts are applied, the method should update the base price via its property setter, automatically keeping all downstream calculations synchronized and valid.

### What You'll Learn
- Managing multiple interdependent properties within a single class
- Implementing read-only dependent properties that automatically track upstream changes
- Integrating discount logic with property setters to preserve data validation

### Requirements & Specifications
Create a `Product` class:

1. **Constructor (`__init__`)**:
   - Parameters: `name`, `price`, `tax_rate` (default = `0.1` for 10%)

2. **Property `price`**:
   - Getter: returns `self._price`
   - Setter: if `value < 0`, print `"Price cannot be negative."` and don't update. Otherwise set `self._price = value`.

3. **Property `tax_rate`**:
   - Getter: returns `self._tax_rate`
   - Setter: if `value < 0` or `value > 1`, print `"Tax rate must be between 0 and 1."` and don't update. Otherwise set `self._tax_rate = value`.

4. **Property `final_price`** (read-only — no setter):
   - Returns `self._price * (1 + self._tax_rate)`

5. **Method**:
   - `apply_discount(percent)`:
     - If `percent < 0` or `percent > 100`, print `"Invalid discount."` and return.
     - Set `self.price = self._price * (1 - percent / 100)` (uses the setter for validation).

### Sample Run
```python
prod = Product("Headphones", 1000, 0.18)
print(prod.price)        # 1000
print(prod.final_price)  # 1180.0

prod.apply_discount(10)
print(prod.price)        # 900.0
print(prod.final_price)  # 1062.0

prod.price = -50         # Price cannot be negative.
print(prod.price)        # 900.0 (unchanged)
```
