import os
from datetime import datetime


class BankAccount:

    def __init__(self):
        self.balance = 0
        self.transactions = []

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def show_menu(self):
        print("\n========= BANK MENU =========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        print("=============================")

    def show_balance(self):
        print(f"\n💰 Current Balance: {self.balance}")

    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                print("❌ Invalid amount")
                return

            self.balance += amount
            self.transactions.append(
                f"{datetime.now()} - Deposited {amount}"
            )

            print(f"✅ {amount} credited successfully")

        except ValueError:
            print("❌ Please enter a valid number")

    def withdraw(self):
        try:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("❌ Invalid amount")
                return

            if amount > self.balance:
                print("❌ Insufficient balance")
                return

            self.balance -= amount
            self.transactions.append(
                f"{datetime.now()} - Withdrawn {amount}"
            )

            print(f"✅ {amount} debited successfully")

        except ValueError:
            print("❌ Please enter a valid number")

    def show_transactions(self):
        print("\n===== Transaction History =====")

        if not self.transactions:
            print("No transactions yet")
            return

        for t in self.transactions:
            print(t)

    def run(self):
        while True:
            self.show_menu()

            try:
                choice = int(input("Select option: "))

                if choice == 1:
                    self.show_balance()

                elif choice == 2:
                    self.deposit()

                elif choice == 3:
                    self.withdraw()

                elif choice == 4:
                    self.show_transactions()

                elif choice == 5:
                    print("\n👋 Thank you for using our banking system")
                    break

                else:
                    print("❌ Invalid choice")

            except ValueError:
                print("❌ Please enter a number")


if __name__ == "__main__":
    app = BankAccount()
    app.run()