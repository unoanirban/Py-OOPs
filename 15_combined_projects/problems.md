# Capstone Projects: Putting It All Together

These projects combine everything you've learned — classes, inheritance, encapsulation, composition, polymorphism, abstract classes, and dunder methods — into complete, working systems.

> **Challenge level:** These are deliberately more complex. You're designing a whole system, not just one class. Plan your class structure before coding. Think about: what objects exist? What data does each own? How do they interact?

---

## Project 1 — Library Management System

### Problem Statement
A municipal library requires a comprehensive catalog and circulation system. The application must track books, registered patrons, borrowing transactions, and overdue penalty fees. 

The system operates under several core institutional rules:
1. Every book has an ISBN, title, author, and availability status.
2. A patron (`Member`) can borrow a maximum of 3 books simultaneously and is prohibited from borrowing any new books if they have unpaid overdue fines.
3. When a patron returns a book past its due date, the library assesses an overdue fine calculated at $0.50 per day overdue. The patron must be able to make payments against outstanding fines.
4. The central `Library` system coordinates inventory and memberships, supports case-insensitive catalog searches matching either title or author keywords, queries available shelf stock, and coordinates borrow and return operations with full validation guards.

### What You'll Learn
- Integrating encapsulation, dunder methods (`__str__`), and multi-class composition
- Synchronizing state between multiple domain models (`Book`, `Member`, and `Library`)
- Implementing penalty fee calculations, threshold validation, and case-insensitive catalog search queries

### Classes & Architecture Requirements

**`Book`**:
- Attributes: `isbn`, `title`, `author`, `available` (bool, default True)
- `__str__`: Returns `"'<title>' by <author> [ISBN: <isbn>]"`
- `borrow()`: Sets `available = False`
- `return_book()`: Sets `available = True`

**`Member`**:
- Attributes: `member_id`, `name`, `borrowed = []`, `fines = 0.0`
- `can_borrow()`: Returns True if `len(borrowed) < 3` and `fines == 0`
- `add_fine(days_overdue)`: Adds `days_overdue * 0.50` to fines.
- `pay_fine(amount)`: Reduces fines by amount (min 0). Returns remaining fine.
- `__str__`: Returns `"<name> (ID: <member_id>) | Books: <count> | Fine: $<fines>"`

**`Library`**:
- Attributes: `name`, `catalog = {}` (isbn → Book), `members = {}` (id → Member)
- `add_book(book)`, `register_member(member)`
- `borrow_book(member_id, isbn)`: Full validation + updates both book and member.
- `return_book(member_id, isbn, days_overdue=0)`: Restore + apply fine if needed.
- `search(query)`: Returns list of books whose title or author contains the query (case-insensitive).
- `get_available_books()`: Returns list of all available books.

### Sample Run
```python
lib = Library("Central Library")

b1 = Book("001", "Python Crash Course", "Eric Matthes")
b2 = Book("002", "Clean Code", "Robert Martin")
b3 = Book("003", "The Pragmatic Programmer", "Hunt & Thomas")

m1 = Member("M01", "Rahul")
m2 = Member("M02", "Priya")

lib.add_book(b1); lib.add_book(b2); lib.add_book(b3)
lib.register_member(m1); lib.register_member(m2)

lib.borrow_book("M01", "001")    # Rahul borrowed 'Python Crash Course'
lib.borrow_book("M01", "002")    # Rahul borrowed 'Clean Code'

print(m1)    # Rahul (ID: M01) | Books: 2 | Fine: $0.0
print(b1)    # 'Python Crash Course' by Eric Matthes [ISBN: 001]

results = lib.search("python")
print(len(results))   # 1

lib.return_book("M01", "001", days_overdue=4)   # 4 * $0.50 = $2 fine
print(m1)    # Rahul (ID: M01) | Books: 1 | Fine: $2.0
m1.pay_fine(2.0)
print(m1)    # Rahul (ID: M01) | Books: 1 | Fine: $0.0
```

---

## Project 2 — ATM System

### Problem Statement
A financial banking infrastructure requires a secure Automated Teller Machine (ATM) software core capable of processing account withdrawals across different financial product types. 

The system must satisfy strict banking security and policy rules:
1. Every account is protected by an encapsulated private PIN (`__pin`) and authenticated prior to balance queries or fund disbursements.
2. Account types have fundamentally different withdrawal rules:
   - `SavingsAccount`: Enforces a mandatory minimum balance threshold (e.g., $500). A withdrawal is rejected if it would deplete funds below this safety reserve.
   - `CurrentAccount`: Provides an approved overdraft facility (e.g., up to $2,000 in credit). The balance is permitted to turn negative down to the overdraft limit.
3. The `ATM` terminal manages a finite physical cash vault (`cash_reserve`). When a user requests a withdrawal, the ATM validates PIN credentials, checks its own physical cash reserves, requests the underlying account to process the withdrawal under its specific rules, and decrements its internal vault upon transaction success.

### What You'll Learn
- Defining abstract base classes (`BankAccount` with ABC) with abstract withdrawal contracts
- Protecting sensitive credentials (PIN) using private attributes and authentication methods
- Modeling specialized banking products (`SavingsAccount` vs. `CurrentAccount`) with divergent business constraints
- Managing physical asset constraints (ATM vault cash reserve) during account settlements

### Classes & Architecture Requirements

**Abstract base class `BankAccount` (use ABC)**:
- Constructor: `__init__(self, account_number, holder, pin, balance=0)`
- Store `pin` as private: `self.__pin`
- `authenticate(pin)`: Returns True if pin matches (no lockout for simplicity here).
- `deposit(amount)`: Validates and adds to balance.
- `@abstractmethod withdraw(amount, pin)`: Subclasses implement this.
- `get_balance(pin)`: Returns balance if authenticated, else `None`.

**`SavingsAccount(BankAccount)`**:
- Constructor adds `min_balance=500`
- `withdraw(amount, pin)`: Only allows withdrawal if balance won't drop below `min_balance`.

**`CurrentAccount(BankAccount)`**:
- Constructor adds `overdraft_limit=2000`
- `withdraw(amount, pin)`: Allows going negative down to `-overdraft_limit`.

**`ATM`**:
- Constructor: `__init__(self, cash_reserve=100000)`
- Attribute: `self.accounts = {}` (account_number → BankAccount)
- `add_account(account)`
- `withdraw(account_number, pin, amount)`:
  - Check ATM has enough cash.
  - Try to withdraw from account.
  - If successful, reduce `cash_reserve`, print receipt.
  - Print failure reason otherwise.

### Sample Run
```python
atm = ATM(cash_reserve=50000)

savings = SavingsAccount("SAV001", "Rahul", "1234", balance=5000)
current = CurrentAccount("CUR001", "Priya", "5678", balance=1000)

atm.add_account(savings)
atm.add_account(current)

atm.withdraw("SAV001", "1234", 2000)   # Success — balance becomes 3000
atm.withdraw("SAV001", "1234", 3000)   # Fails — would drop below min_balance 500
atm.withdraw("CUR001", "5678", 2500)   # Success — overdraft allowed (balance = -1500)
atm.withdraw("CUR001", "9999", 100)    # Wrong PIN
```

---

## Project 3 — Mini E-Commerce System

### Problem Statement
A digital retail storefront requires an end-to-end shopping and checkout system. The platform must manage merchandise inventory, aggregate items in customer shopping carts, support pluggable payment processors, and orchestrate final order confirmation.

The system must handle the full transaction lifecycle:
1. Products maintain live inventory stock levels and support inventory reservation upon checkout.
2. A customer cart tracks selected items and quantities, automatically computing order totals and exposing container dunder methods (`__len__`, `__str__`).
3. Payment execution must be polymorphic: the checkout workflow should accept any payment processor deriving from an abstract `PaymentMethod` interface (e.g., `CardPayment` or `UPIPayment`).
4. When checkout completes successfully, warehouse inventory is permanently reduced, an order record is appended to the customer's history, the cart is cleared, and an order receipt is issued.

### What You'll Learn
- Combining abstract classes, polymorphism, encapsulation, and dunder methods into a unified e-commerce architecture
- Implementing pluggable payment processors using abstract strategy contracts
- Orchestrating multi-entity state transactions across catalog inventory, cart items, and order history

### Classes & Architecture Requirements

**`Product`**:
- Attributes: `product_id`, `name`, `price`, `stock`
- `__str__`: Returns `"<name> — $<price> (Stock: <stock>)"`
- `reserve(qty)`: Reduces stock if available, returns True/False.

**Abstract base class `PaymentMethod` (use ABC)**:
- `@abstractmethod pay(amount)`: Returns a transaction receipt dict `{"status": "success"/"failed", "amount": ..., "method": ...}`.

**`CardPayment(PaymentMethod)`**:
- Constructor: `__init__(self, card_number)`
- `pay(amount)`: Simulates success. Returns receipt with `"method": "Card"`.

**`UPIPayment(PaymentMethod)`**:
- Constructor: `__init__(self, upi_id)`
- `pay(amount)`: Simulates success. Returns receipt with `"method": "UPI"`.

**`Cart`**:
- `__init__(self, owner_name)`
- `self.items = {}` (Product → quantity)
- `add_item(product, qty)`, `remove_item(product_id)`, `get_total()`, `__len__`, `__str__`

**`Customer`**:
- Constructor: `__init__(self, name)`
- `self.cart = Cart(name)`, `self.orders = []`
- `checkout(payment_method)`:
  - If cart empty, return None.
  - Call `payment_method.pay(total)`.
  - If success: reserve stock for all items, create order dict, clear cart.
  - Print receipt.

### Sample Run
```python
p1 = Product("P01", "Python Book", 400, 10)
p2 = Product("P02", "Laptop Stand", 1500, 5)

card = CardPayment("4111-1111-1111-4444")
upi = UPIPayment("rahul@upi")

customer = Customer("Rahul")
customer.cart.add_item(p1, 2)
customer.cart.add_item(p2, 1)

print(len(customer.cart))   # 3 items total
print(customer.cart)        # Cart summary

customer.checkout(card)     # Paid $2300 via Card. Order confirmed!
print(p1.stock)             # 8
```
