""" 
Variables- contaires or labelled box that stores and references data of different types

types
-local varibales
-global variables
 
THIS IS REVISION
"""

FirstName="John"
LastName="Doe"
Age = 25

#SecondName= input("please enter your second name: ")

#print(FirstName, LastName, SecondName, Age, sep= "<****> " )
print("================================================")


#Example Two 
#variables
my_variable_name = 'FreeCodeCamp'
user_age = 25

#Print function
"""
    PRINT FUNCTION
-It is used to output data on the terninal

Python automatically adds a space between each item when you separate them with commas. This is helpful when you want to print several pieces of information together.
"""

print('My Favourite colors are', 'red', 'blue', 'pink'
      )


print("================================================")



#Data types
"""
DATA TYPES

Are used to describe the kind of value of a certain variabe

    - boolean: stores either True or False
    - number [ int, float, complex]
    - Strings
    - lists
    - tuples
    - dictionaries
    - set
"""
# number [ int, float, complex]
# int:  -ve infinity to +ve infinity
num1 = 10
num2 = -11
num3 = "100"
num4 = int(num3) # type casting


# float(decimal number): -ve infinity to +ve infinity  
lat = -0.234
lng = 38.456
num3 = "3.1456"
num4 = float(num3) # type casting

# complex: eg square root of 2 =>
root = 2j

compNum = complex(4) 
output = type(num4)
print
print(output)

#2. STRINGS
#A sequence of characters enclosed in singe or double quotation marks that represents a text

name = "Alex Crew"
my_string_var = "Hello!"
print("string :", my_string_var)

# LIST

#TUPLE

#SET

#DICTIONARY

#RANGE


#Augmented Assignment
"""
Augmented assignment combines a binary operation with an assignment in one step. It takes a variable, applies an operation to it with another value, and stores the result back into the same variable.

The basic syntax of an augmented assignment looks like this:

variable <operator>= value

"""
#Example with Augmented assn
#Addition
num1 = 10
num1 +=5 #Addition assignment operator
print(num1)

#Subtraction assignment operator
count1 = 20
count1 -= 2
print(count1)

#Multiplication
product = 65
product *= 7

print(product) # 455

#Division
price = 100
price /= 4

print(price) # 25.0

# floor division operator (//=)
total_pages = 23
total_pages //= 5

print(total_pages) # 4


#modulo assignment operator (%=)
bits = 35
bits %= 2

print(bits) # 1

#exponentiation assignment operator (**=
power = 2
power **= 3

print(power) # 8


# Example without
num1 = 10
num1 = num1 +5 

print(num1)

"""
# NB same case apply for strings but  other operators are not supported eg: subraction assignment operator, Division assignment operator
# """
#eg
greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello

