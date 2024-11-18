class ATM:
    bank_name = "The-Fundsfinder_Gram"  # Class variable

    def __init__(self, user):
        self.user = user  # Instance variable for authenticated user
        self.session_deposits = 0
        self.session_withdrawals = 0

    def check_balance(self):
        print(f"Your current balance is: ${self.user.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be positive.")
            return
        self.user.balance += amount
        self.session_deposits += amount
        print(f"${amount} deposited. New balance: ${self.user.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be positive.")
            return
        if amount > self.user.balance:
            print("Insufficient balance!")
            return
        self.user.balance -= amount
        self.session_withdrawals += amount
        print(f"${amount} withdrawn. New balance: ${self.user.balance}")

    def change_pin(self, current_pin, new_pin):
        if self.user.pin == current_pin:
            if len(str(new_pin)) == 4:
                self.user.pin = new_pin
                print("PIN successfully updated.")
            else:
                print("New PIN must be a 4-digit number.")
        else:
            print("Incorrect current PIN.")
