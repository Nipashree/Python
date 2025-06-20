class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

def main():
    print("Welcome to Simple Bank!")
    name = input("Enter your name to create an account: ")
    account = BankAccount(name)
    
    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
