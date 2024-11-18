# The-Fundsfinder_Gram_ATM-Machine
## Author 
[Abdul-Majeed Saidatu](abdulmajeedsaidatu@gmail.com)

## Project Overview
Welcome to The-Fundsfinder_Gram_ATM-Machine Simulator!
This project allows users to simulate an ATM, where they can check their balance, deposit or withdraw money, and change their PIN. It is built using Object-Oriented Programming (OOP) to keep the code organized and manageable.

The essential Object-Oriented Programming(OOP) Concepts used fot the development of this ATM Machine are:
Classes and Instances: The simulator uses classes, like the ATM class, to manage user interactions and transactions. This makes the code easier to maintain.
Instance Variables and Methods: Each user has their own balance and PIN stored as instance variables. Methods such as check_balance(), deposit_funds(), and withdraw_funds() perform actions that update these values.
Class Methods and Static Methods: A class method keeps track of shared information, like the maximum number of PIN entry attempts. Static methods handle tasks like validating user input without needing specific user data.
Inheritance: The simulator can be expanded by allowing an ATMUser class to inherit from a User class, using the super() method to properly set up user data.
Magic Methods and Property Decorators: Magic methods (like __str__) determine how the ATM object is displayed when printed. Property decorators calculate the account balance in real-time for better security.
This project uses these OOP principles to create a secure, interactive, and easily expandable ATM simulation.

!(https://th.bing.com/th/id/R.cfd45d3f1ac1fe4d2288f9132b11242d?rik=kXJxNsi9ybv8pw&riu=http%3a%2f%2fatmbrokerage.com%2fwp-content%2fuploads%2f2018%2f03%2fATM-machine-.png&ehk=xHe306qvj69Eq77MV86MHtixHrc%2f9uwvUG3tohvCzI4%3d&risl=&pid=ImgRaw&r=)