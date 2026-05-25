"""
    ******** OBJECT-ORIENTED PROGRAMMING ********
- It's a way of organising code that uses objects and classes to represent real-world entities and behaviours
It contains four key principles:

 ======= Encapsulation =======
    
- Encapsulation means combining data and methods into one class and restricting direct access to internal data.

     > Public methods control access to private data.
     > Private attributes use double underscores (__).

 ======= Inheritance =======

 Inheritance allows code reusability - it allows classes to use methods and properties from another class
 subclasses(child classes) can use attributes and methods of a base class(parent class)
 > It also creates class hierarchies 
 > customizes behaviours without rewriting by either extending existing methods or overring them

 ======= Polymorphism =======

 Polymorphism alllows same methods or functions to be used on objects differently
 ======= Abstraction =======
Importance of OOP
 - Help organise code better - supports encapsulation
 - Enables code reusability through inheritance
 - Data security through encapsulation - this prevents unauthorized or accidental changes on sensitive data
 -


"""
# ***** 1. Encapsulation Example ******
# Class Wallet with balance attribute set to private

# Getting the __balance value by defining the get_balance method
class Wallet:
   def __init__(self, balance):
       self.__balance = balance

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount

   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount
  
   def get_balance(self):
       return self.__balance


acct_one = Wallet(100)
acct_one.deposit(50)
print(acct_one.get_balance()) # 150

acct_two = Wallet(450)
acct_two.withdraw(28)
print(acct_two.get_balance()) # 422

acct_two.deposit(150)
print(acct_two.get_balance()) # 572

# class Wallet with __Validate set to private
class Wallet:
   def __init__(self):
       self.__balance = 0

   def __validate(self, amount):
       if amount < 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       self.__balance += amount

   def withdraw(self, amount):
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount

   def get_balance(self):
       return self.__balance

acct_one = Wallet()
acct_one.deposit(3)
print(acct_one.get_balance()) # 3

acct_one.deposit(50)
print(acct_one.get_balance()) # 53

acct_one.deposit(-4)  # ValueError: Amount must be positive
acct_one.withdraw(-8) # ValueError: Amount must be positive
acct_one.withdraw(58) # ValueError: Insufficient funds

# **** 2. Inheritance Example****



"""
======= GETTERS, SETTERS & PROPERTY ========

- Getters and setters are used to safely access and modify class attributes. 
- The setter can also validate data before updating the attribute.

- properties are what tie these getters and setters together so you can write logic while still using dot notation.
- The @property decorator creates a getter, while @property_name.setter creates a setter

Deleters let one define what happens when an attribute is deleted. Its created by @property_name.deleter

"""

# Example using getters
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property # Makes radius method/function a property
    def radius(self): # A getter to get the radius
        return self._radius
  
    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)

print(my_circle.radius) # 3
print(my_circle.area) # 28.26

# Example using setters
class Circle:
    def __init__(self, radius):
        self.radius = radius # Calling the setter

    @property
    def radius(self):  # A getter to get the radius
        return self._radius

    @radius.setter 
    def radius(self, value):  # A setter to set the radius
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

my_circle = Circle(3)
print('Initial radius:', my_circle.radius) # Initial radius: 3

my_circle.radius = 8
print('After modifying the radius:', my_circle.radius) # After modifying the radius: 8


# Example using deleter

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius

# Create circle object with a radius
my_circle = Circle(33)
print("Initial radius:", my_circle.radius)  # 33

# Delete the radius
# This calls the deleter
del my_circle.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!

# Try to access radius after deletion
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error:", e) # Error: 'Circle' object has no attribute '_radius'