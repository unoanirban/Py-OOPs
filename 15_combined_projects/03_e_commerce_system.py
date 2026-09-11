"""
## Project 3 — E-Commerce Engine with Polymorphic Checkout

### System Specifications
1. **Class `Product`**:
   - `__init__(product_id: str, title: str, price: float, stock: int)`
   - Properties ensuring `price > 0` and `stock >= 0`.
   - Method `reserve(qty: int) -> bool`.
2. **Class `Cart`**:
   - Implements `__len__()` (total item count) and `__getitem__()`.
   - Methods: `add_item(product, qty)`, `remove_item(product_id)`, `get_total()`.
3. **Abstract Base Class `PaymentGateway(ABC)`**:
   - `@abstractmethod def pay(self, amount: float) -> dict`.
   - Concrete implementations:
     - `UPIPayment(vpa)`
     - `CardPayment(card_no, cvv, exp)`
     - `CashOnDelivery(delivery_address)`
4. **Class `Order`**:
   - `__init__(order_id: str, customer_name: str, items: list[dict], subtotal: float, payment_receipt: dict)`
   - Method `generate_invoice() -> str`.
5. **Class `Customer`**:
   - Owns a `Cart`.
   - Method `checkout(payment_gateway: PaymentGateway, coupon_percent: float = 0.0) -> Optional[Order]`.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:
