from user import User
from atm import ATM
from utilities import Utilities

# Create a sample user
user = User("Mariam", 1234)

# Initialize ATM
atm = ATM(user)

# Start the program
print("Welcome to The-Fundsfinder_Gram!")
attempts = 3

# Authentication
while attempts > 0:
    pin = Utilities.get_valid_input("Enter your PIN: ", int)
    if atm.user.pin == pin:
        print("Authentication successful!")
        break
    attempts -= 1
    print(f"Incorrect PIN. {attempts} attempts left.")
else:
    print("Too many incorrect attempts. Access blocked.")
    exit()

# Main menu
while True:
    print("\nMain Menu:")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Change PIN")
    print("5. Exit")

    choice = Utilities.get_valid_input("Choose an option: ", int)

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = Utilities.get_valid_input("Enter amount to deposit: ", int)
        atm.deposit(amount)
    elif choice == 3:
        amount = Utilities.get_valid_input("Enter amount to withdraw: ", int)
        atm.withdraw(amount)
    elif choice == 4:
        current_pin = Utilities.get_valid_input("Enter current PIN: ", int)
        new_pin = Utilities.get_valid_input("Enter new 4-digit PIN: ", int)
        atm.change_pin(current_pin, new_pin)
    elif choice == 5:
        print("Thank you for using The-Fundsfinder_Gram!")
        print(f"Total Deposits: ${atm.session_deposits}")
        print(f"Total Withdrawals: ${atm.session_withdrawals}")
        break
    else:
        print("Invalid option. Please try again.")
