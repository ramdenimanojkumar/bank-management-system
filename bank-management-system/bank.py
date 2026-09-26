from abc import ABC, abstractmethod


# ==============================
# ABSTRACT BASE CLASS
# ==============================

class BankAccount(ABC):

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance
        self.transactions = []

    # ==============================
    # DEPOSIT
    # ==============================

    def deposit(self, amount):

        if amount <= 0:
            print("Amount should be greater than 0")
            return

        self.__balance += amount

        self.transactions.append(
            f"Deposited: ₹{amount}"
        )

        print(f"₹{amount} deposited successfully")

    # ==============================
    # GET BALANCE
    # ==============================

    def get_balance(self):
        return self.__balance

    # ==============================
    # INTERNAL BALANCE UPDATE
    # ==============================

    def update_balance(self, amount):
        self.__balance += amount

    # ==============================
    # ABSTRACT WITHDRAW METHOD
    # ==============================

    @abstractmethod
    def withdraw(self, amount):
        pass

    # ==============================
    # TRANSACTION HISTORY
    # ==============================

    def show_transactions(self):

        if not self.transactions:
            print("No transactions available")
            return

        print("\n===== TRANSACTION HISTORY =====")

        for transaction in self.transactions:
            print(transaction)

    # ==============================
    # ACCOUNT DETAILS
    # ==============================

    def show_account_details(self):

        print("\n===== ACCOUNT DETAILS =====")
        print("Name:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance: ₹", self.get_balance())


# ==========================================
# SAVINGS ACCOUNT
# ==========================================

class SavingsAccount(BankAccount):

    def __init__(self, name, acc_no, balance, interest_rate):

        super().__init__(name, acc_no, balance)

        self.interest_rate = interest_rate

    # ==============================
    # METHOD OVERRIDING
    # ==============================

    def withdraw(self, amount):

        if amount <= 0:
            print("Amount should be greater than 0")
            return

        if amount > self.get_balance():
            print("Insufficient balance")
            return

        self.update_balance(-amount)

        self.transactions.append(
            f"Withdrawn: ₹{amount}"
        )

        print(f"₹{amount} withdrawn successfully")

    # ==============================
    # ADD INTEREST
    # ==============================

    def add_interest(self):

        interest = (
            self.get_balance()
            * self.interest_rate
            / 100
        )

        self.update_balance(interest)

        self.transactions.append(
            f"Interest added: ₹{interest:.2f}"
        )

        print(
            f"₹{interest:.2f} interest added successfully"
        )


# ==========================================
# CURRENT ACCOUNT
# ==========================================

class CurrentAccount(BankAccount):

    def __init__(
        self,
        name,
        acc_no,
        balance,
        minimum_balance
    ):

        super().__init__(
            name,
            acc_no,
            balance
        )

        self.minimum_balance = minimum_balance

    # ==============================
    # METHOD OVERRIDING
    # ==============================

    def withdraw(self, amount):

        if amount <= 0:
            print("Amount should be greater than 0")
            return

        remaining_balance = (
            self.get_balance() - amount
        )

        if remaining_balance < self.minimum_balance:
            print(
                "Withdrawal failed!"
            )

            print(
                f"Minimum balance of ₹{self.minimum_balance} "
                f"must be maintained."
            )

            return

        self.update_balance(-amount)

        self.transactions.append(
            f"Withdrawn: ₹{amount}"
        )

        print(
            f"₹{amount} withdrawn successfully"
        )


# ==========================================
# TRANSFER MONEY
# ==========================================

def transfer_money(sender, receiver, amount):

    if amount <= 0:
        print("Transfer amount should be greater than 0")
        return

    if amount > sender.get_balance():
        print("Insufficient balance")
        return

    sender.update_balance(-amount)
    receiver.update_balance(amount)

    sender.transactions.append(
        f"Transferred ₹{amount} to {receiver.name}"
    )

    receiver.transactions.append(
        f"Received ₹{amount} from {sender.name}"
    )

    print(
        f"₹{amount} transferred successfully "
        f"from {sender.name} to {receiver.name}"
    )


# ==========================================
# CREATE ACCOUNTS
# ==========================================

savings = SavingsAccount(
    "Manoj",
    1001,
    5000,
    5
)

current = CurrentAccount(
    "Rahul",
    1002,
    10000,
    2000
)


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("================================")
    print("     BANK MANAGEMENT SYSTEM")
    print("================================")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Add Interest")
    print("5. Transfer Money")
    print("6. Transaction History")
    print("7. Account Details")
    print("8. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    # ==============================
    # DEPOSIT
    # ==============================

    if choice == "1":

        print("\n1. Manoj - Savings")
        print("2. Rahul - Current")

        account_choice = input(
            "Select account: "
        )

        amount = float(
            input("Enter deposit amount: ")
        )

        if account_choice == "1":
            savings.deposit(amount)

        elif account_choice == "2":
            current.deposit(amount)

        else:
            print("Invalid account")

    # ==============================
    # WITHDRAW
    # ==============================

    elif choice == "2":

        print("\n1. Manoj - Savings")
        print("2. Rahul - Current")

        account_choice = input(
            "Select account: "
        )

        amount = float(
            input("Enter withdrawal amount: ")
        )

        if account_choice == "1":
            savings.withdraw(amount)

        elif account_choice == "2":
            current.withdraw(amount)

        else:
            print("Invalid account")

    # ==============================
    # CHECK BALANCE
    # ==============================

    elif choice == "3":

        print("\n1. Manoj")
        print("2. Rahul")

        account_choice = input(
            "Select account: "
        )

        if account_choice == "1":

            print(
                "Manoj Balance: ₹",
                savings.get_balance()
            )

        elif account_choice == "2":

            print(
                "Rahul Balance: ₹",
                current.get_balance()
            )

        else:
            print("Invalid account")

    # ==============================
    # ADD INTEREST
    # ==============================

    elif choice == "4":

        savings.add_interest()

    # ==============================
    # TRANSFER
    # ==============================

    elif choice == "5":

        print("\n1. Manoj → Rahul")
        print("2. Rahul → Manoj")

        transfer_choice = input(
            "Select transfer: "
        )

        amount = float(
            input("Enter transfer amount: ")
        )

        if transfer_choice == "1":

            transfer_money(
                savings,
                current,
                amount
            )

        elif transfer_choice == "2":

            transfer_money(
                current,
                savings,
                amount
            )

        else:
            print("Invalid choice")

    # ==============================
    # TRANSACTION HISTORY
    # ==============================

    elif choice == "6":

        print("\n1. Manoj")
        print("2. Rahul")

        account_choice = input(
            "Select account: "
        )

        if account_choice == "1":

            savings.show_transactions()

        elif account_choice == "2":

            current.show_transactions()

        else:
            print("Invalid account")

    # ==============================
    # ACCOUNT DETAILS
    # ==============================

    elif choice == "7":

        print("\n1. Manoj")
        print("2. Rahul")

        account_choice = input(
            "Select account: "
        )

        if account_choice == "1":

            savings.show_account_details()

        elif account_choice == "2":

            current.show_account_details()

        else:
            print("Invalid account")

    # ==============================
    # EXIT
    # ==============================

    elif choice == "8":

        print("Thank you for using Bank Management System!")
        break

    else:

        print("Invalid choice. Please try again.")