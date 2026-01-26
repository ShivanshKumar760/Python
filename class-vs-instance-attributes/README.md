# Class vs Instance Attributes

**🔗 [View on NeetCode](https://neetcode.io/problems/python-class-vs-instance-attributes/question)**

---

The below example shows a `BankAccount` class with class and instance attributes.

```python
class BankAccount:
    total_accounts = 0    # Class attribute: Shared by ALL accounts
    total_balance = 0     # Class attribute: Tracks bank's total money
    
    def __init__(self, name: str, balance: float):
        self.name = name        # Instance: Each account has unique owner
        self.balance = balance  # Instance: Each account has unique balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
```

1. We use class attributes to track bank-wide information that is shared by all accounts, such as the total number of accounts and the total balance of all accounts.

2. We use instance attributes to track information that is unique to each account, such as the account number and the balance of the account.

#### Challenge

Your task is to implement a `BankAccount` class that effectively uses both class and instance attributes.

The attributes you need to track are:

- The total number of accounts in bank `total_accounts`

- The bank's total balance `total_balance`

- The individual account owner names `name`

- The individual account balances `balance`

You tasks are:

1. Decide which attributes should be class vs instance attributes and add them at their appropriate places

2. Implement the `BankAccount` class

3. Create two accounts, `"Alice"` and `"Bob"` with balances `1000` and `2000` respectively

4. Print the information using the following format:

- `print(f"Alice's balance: <Alice's balance>")`

- `print(f"Bob's balance: <Bob's balance>")`

- `print(f"Total Accounts: <Total Accounts>")`

- `print(f"Total Balance: <Total Balance>")`

#### Expected Output

```
Alice's balance: $1000
Bob's balance: $2000
Total Accounts: 2
Total Balance: $3000
```

Hints

- Think: Does the attribute need to be shared across ALL accounts?

- Class attributes are defined outside `__init__`

- Instance attributes are defined inside `__init__`

- Remember to update class attributes when creating new accounts

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
