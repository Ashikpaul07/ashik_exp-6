#creating class
class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = [] # Stores transaction history
#function to check balance
    def check_balance(self):
        return f"Current balance: ₹{self.balance}"
#function to deposit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            return f"Successfully deposited ₹{amount}. {self.check_balance()}"
        return "Deposit amount must be greater than 0."
#function to withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            return f"Successfully withdrew ₹{amount}. {self.check_balance()}"
        return "Insufficient funds or invalid amount."
#function to view transaction history
    def transaction_history(self):
        if self.transactions:
            return "\n".join(self.transactions)
        return "No transactions yet."
atm = ATM(initial_balance=10000)
print(atm.deposit(5000))
print(atm.withdraw(3000))
print(atm.transaction_history())
print(atm.check_balance())
