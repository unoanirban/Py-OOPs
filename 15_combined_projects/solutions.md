# Solutions: 15 — Capstone Projects

## Project 1 — Library Management System

```python
class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} [ISBN: {self.isbn}]"

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed = []
        self.fines = 0.0

    def can_borrow(self):
        return len(self.borrowed) < 3 and self.fines == 0.0

    def add_fine(self, days_overdue):
        self.fines += days_overdue * 0.50

    def pay_fine(self, amount):
        self.fines = max(0, self.fines - amount)
        return self.fines

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) | Books: {len(self.borrowed)} | Fine: ${self.fines}"


class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = {}
        self.members = {}

    def add_book(self, book):
        self.catalog[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.catalog.get(isbn)

        if not member:
            print("Member not found.")
            return False
        if not book:
            print("Book not found.")
            return False
        if not book.available:
            print(f"'{book.title}' is not available.")
            return False
        if not member.can_borrow():
            print(f"{member.name} cannot borrow more books.")
            return False

        book.borrow()
        member.borrowed.append(book)
        print(f"{member.name} borrowed {book}.")
        return True

    def return_book(self, member_id, isbn, days_overdue=0):
        member = self.members.get(member_id)
        book = self.catalog.get(isbn)

        if not member or not book:
            print("Member or book not found.")
            return False
        if book not in member.borrowed:
            print("This member did not borrow this book.")
            return False

        book.return_book()
        member.borrowed.remove(book)
        if days_overdue > 0:
            member.add_fine(days_overdue)
            print(f"{member.name} returned {book}. Fine: ${days_overdue * 0.50}")
        else:
            print(f"{member.name} returned {book}. No fine.")
        return True

    def search(self, query):
        query = query.lower()
        return [b for b in self.catalog.values()
                if query in b.title.lower() or query in b.author.lower()]

    def get_available_books(self):
        return [b for b in self.catalog.values() if b.available]


# Try it out
lib = Library("Central Library")

b1 = Book("001", "Python Crash Course", "Eric Matthes")
b2 = Book("002", "Clean Code", "Robert Martin")
b3 = Book("003", "The Pragmatic Programmer", "Hunt & Thomas")
m1 = Member("M01", "Rahul")
m2 = Member("M02", "Priya")

for b in [b1, b2, b3]: lib.add_book(b)
for m in [m1, m2]: lib.register_member(m)

lib.borrow_book("M01", "001")
lib.borrow_book("M01", "002")
print(m1)

results = lib.search("python")
print(f"Search results: {len(results)}")

lib.return_book("M01", "001", days_overdue=4)
print(m1)
m1.pay_fine(2.0)
print(m1)
```

---

## Project 2 — ATM System

```python
from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, holder, pin, balance=0):
        self.account_number = account_number
        self.holder = holder
        self.__pin = pin
        self.balance = balance

    def authenticate(self, pin):
        return pin == self.__pin

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return False
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")
        return True

    @abstractmethod
    def withdraw(self, amount, pin):
        pass

    def get_balance(self, pin):
        if self.authenticate(pin):
            return self.balance
        print("Wrong PIN.")
        return None


class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder, pin, balance=0, min_balance=500):
        super().__init__(account_number, holder, pin, balance)
        self.min_balance = min_balance

    def withdraw(self, amount, pin):
        if not self.authenticate(pin):
            print("Wrong PIN.")
            return False
        if self.balance - amount < self.min_balance:
            print(f"Cannot withdraw — balance would drop below minimum ${self.min_balance}.")
            return False
        self.balance -= amount
        print(f"Withdrew ${amount}. Balance: ${self.balance}")
        return True


class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder, pin, balance=0, overdraft_limit=2000):
        super().__init__(account_number, holder, pin, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount, pin):
        if not self.authenticate(pin):
            print("Wrong PIN.")
            return False
        if self.balance - amount < -self.overdraft_limit:
            print(f"Exceeds overdraft limit of ${self.overdraft_limit}.")
            return False
        self.balance -= amount
        print(f"Withdrew ${amount}. Balance: ${self.balance}")
        return True


class ATM:
    def __init__(self, cash_reserve=100000):
        self.cash_reserve = cash_reserve
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def withdraw(self, account_number, pin, amount):
        if account_number not in self.accounts:
            print("Account not found.")
            return
        if amount > self.cash_reserve:
            print("ATM has insufficient cash.")
            return
        account = self.accounts[account_number]
        if account.withdraw(amount, pin):
            self.cash_reserve -= amount
            print(f"ATM dispensed ${amount}. ATM cash left: ${self.cash_reserve}")


# Try it out
atm = ATM(cash_reserve=50000)
savings = SavingsAccount("SAV001", "Rahul", "1234", balance=5000)
current = CurrentAccount("CUR001", "Priya", "5678", balance=1000)

atm.add_account(savings)
atm.add_account(current)

atm.withdraw("SAV001", "1234", 2000)   # Success
atm.withdraw("SAV001", "1234", 3000)   # Fails — min balance
atm.withdraw("CUR001", "5678", 2500)   # Success — overdraft
atm.withdraw("CUR001", "9999", 100)    # Wrong PIN
```

---

## Project 3 — Mini E-Commerce System

```python
from abc import ABC, abstractmethod


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} — ${self.price} (Stock: {self.stock})"

    def reserve(self, qty):
        if qty > self.stock:
            print(f"Not enough stock for {self.name}.")
            return False
        self.stock -= qty
        return True


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return {"status": "success", "amount": amount, "method": f"Card (*{self.card_number[-4:]})"}


class UPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        return {"status": "success", "amount": amount, "method": f"UPI ({self.upi_id})"}


class Cart:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.items = {}

    def add_item(self, product, qty):
        if qty > product.stock:
            print(f"Only {product.stock} units of {product.name} available.")
            return
        self.items[product] = self.items.get(product, 0) + qty
        print(f"Added {product.name} x{qty}")

    def remove_item(self, product_id):
        for p in list(self.items.keys()):
            if p.product_id == product_id:
                del self.items[p]
                print(f"Removed {p.name} from cart.")
                return
        print("Item not found in cart.")

    def get_total(self):
        return sum(p.price * qty for p, qty in self.items.items())

    def __len__(self):
        return sum(self.items.values())

    def __str__(self):
        lines = [f"Cart ({self.owner_name}):"]
        for p, qty in self.items.items():
            lines.append(f"  {p.name} x{qty} — ${p.price * qty}")
        lines.append(f"  Total: ${self.get_total()}")
        return "\n".join(lines)


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart(name)
        self.orders = []

    def checkout(self, payment_method):
        if len(self.cart) == 0:
            print("Cart is empty.")
            return None

        total = self.cart.get_total()
        receipt = payment_method.pay(total)

        if receipt["status"] == "success":
            for product, qty in self.cart.items.items():
                product.reserve(qty)
            order = {"items": list(self.cart.items.keys()), "total": total, "receipt": receipt}
            self.orders.append(order)
            self.cart.items = {}
            print(f"Order confirmed! Paid ${total} via {receipt['method']}.")
            return order
        else:
            print("Payment failed.")
            return None


# Try it out
p1 = Product("P01", "Python Book", 400, 10)
p2 = Product("P02", "Laptop Stand", 1500, 5)

card = CardPayment("4111-1111-1111-4444")
upi = UPIPayment("rahul@upi")

customer = Customer("Rahul")
customer.cart.add_item(p1, 2)
customer.cart.add_item(p2, 1)

print(f"Items in cart: {len(customer.cart)}")
print(customer.cart)

customer.checkout(card)
print(f"p1 stock after: {p1.stock}")    # 8
print(f"Cart empty: {len(customer.cart) == 0}")   # True

# Try with UPI:
customer.cart.add_item(p1, 1)
customer.checkout(upi)
```
