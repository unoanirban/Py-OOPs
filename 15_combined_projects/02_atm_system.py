"""
## Project 2 — Multi-Tier ATM & Banking Core

### System Specifications
1. **Abstract Base Class `BankAccount(ABC)`**:
   - Constructor: `__init__(account_number: str, holder_name: str, pin: str, initial_balance: float)`
   - Encapsulated private attributes: `__balance`, `__pin`, `__is_locked`, `__failed_attempts`.
   - Method: `authenticate(pin: str) -> bool` (3-attempt lockout).
   - Method: `deposit(amount: float) -> bool`.
   - `@abstractmethod def withdraw(self, amount: float, pin: str) -> bool`.
   - Method: `get_balance(pin: str) -> Optional[float]`.
2. **Subclass `SavingsAccount(BankAccount)`**:
   - Constructor: includes `min_balance: float = 100.0`, `interest_rate: float = 0.04`.
   - Overrides `withdraw()`: withdrawal is rejected if balance after withdrawal drops below `min_balance`.
   - Method `apply_interest() -> float`: Adds annual interest to balance and returns interest amount.
3. **Subclass `CurrentAccount(BankAccount)`**:
   - Constructor: includes `overdraft_limit: float = 500.0`.
   - Overrides `withdraw()`: allows balance to go negative down to `-overdraft_limit`.
4. **Class `ATM`**:
   - Composes access to a bank network `accounts: dict[str, BankAccount]`.
   - Attributes: `cash_reserve: float = 50000.0`.
   - Methods:
     - `insert_card_and_withdraw(account_number: str, pin: str, amount: float) -> dict`:
       - Checks ATM cash reserve.
       - Authenticates account and executes withdrawal.
       - Dispenses cash and returns transaction receipt.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:
