class User:
    def __init__(self, name, pin, balance=5000):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        return f"User({self.name}, Balance: ${self.balance})"


class AdminUser(User):
    def __init__(self, name, pin, balance=5000, admin_code="ADMIN123"):
        super().__init__(name, pin, balance)
        self.admin_code = admin_code

    def reset_user_balance(self, user):
        user.balance = 0
        print(f"{user.name}'s balance has been reset to $0.")
