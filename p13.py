
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs. {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: Rs. {amount:.2f}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : Rs. {self.__balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number,
                 balance=0, interest_rate=5):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    # Method overriding
    def deposit(self, amount):
        print("[Savings Account]")
        super().deposit(amount)

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        super().deposit(interest)
        print(f"Interest added: Rs. {interest:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number,
                 balance=0, overdraft_limit=2000):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    # Method overriding
    def withdraw(self, amount):
        print("[Current Account]")

        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.get_balance() + self.overdraft_limit:
            # Use the parent's withdrawal logic when
            # the amount is within the available balance.
            if amount <= self.get_balance():
                super().withdraw(amount)
            else:
                overdraft_used = amount - self.get_balance()
                super().withdraw(self.get_balance())
                print(f"Overdraft used: Rs. {overdraft_used:.2f}")
                print("Note: Overdraft usage is tracked separately.")
        else:
            print("Overdraft limit exceeded!")


def show_account(account):
    # Polymorphism: works with different account types
    account.display_details()
    print("-" * 40)


if __name__ == "__main__":
    print("=" * 40)
    print("       ENCAPSULATED BANKING SYSTEM")
    print("=" * 40)

    savings = SavingsAccount("Rahul", "S101", 10000, 5)
    current = CurrentAccount("Priya", "C201", 5000, 2000)

    print("\n--- Savings Account Transactions ---")
    savings.display_details()
    savings.deposit(2000)
    savings.withdraw(1500)
    savings.add_interest()
    print(f"Final Savings Balance: Rs. {savings.get_balance():.2f}")

    print("\n--- Current Account Transactions ---")
    current.display_details()
    current.deposit(1000)
    current.withdraw(7000)
    print(f"Final Current Balance: Rs. {current.get_balance():.2f}")

    print("\n--- Polymorphic Account Display ---")
    for account in [savings, current]:
        show_account(account)
