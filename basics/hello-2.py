"""
- Operators & Operands
    - arithmetic operators:  +, -, /, //, **, *
    - comparison operators: ==, !=, <, >, <=,>=
    - boolean operators: and, or, not (Truth table)
    - is operator: identity operator
    - in membership operator 
    - ternary operator  
    - binary operators  ( |, &, ^, <<, >> )

- Data structures
    - Data Types: 
        - boolean
        - number [ int, float, complex]
        - lists
        - tuples
        - dictionaries
        - set


"""

output = "" # general output variable
num1 = 10
num2 = 12

# Operators & Operands

#  arithmetic operators:  +, -, /, //, **, *, %
output = num1 + num2 # addition
output = num1 - num2 # subtraction
output = num1 / num2 # division
output = num1 // num2 # floor division
output = num1 * num2 # multiplication
num1 = 10
num2 = 2
output = num1 ** num2 # power
output = num1 % num2 # modulus, the remainder when the value of left is divided by the value on the right

# comparison operators: ==, !=, <, >, <=,>=
firstName = "John"
lastName = "Doe"

num1 = 10
num2 =11
num3 =10

output = firstName == lastName # equality check
output = firstName != lastName # not equality check
output =  num1 > num2 # greater than 
output =  num1 < num2 # less than 
output =  num1 >= num2 # greater than or equal to
output =  num1 <= num2 # less than or equal to

"""
boolean operators: and, or, not (Truth table)
- and: both operands must be true to get a true else false
- or: atleast one must be true
"""
firstName = "John"
secondName = "John"
lastName = "Doe"

num1 = 10
num2 =11
num3 =10

isUserLoggedIn = True
isDarkMode = False

output = (firstName == secondName) and (secondName == lastName)# strict and
output = isUserLoggedIn and isDarkMode # strict and
output = isDarkMode or isUserLoggedIn # flexible OR operator
output = not (isDarkMode or isUserLoggedIn) # not operator-> opposite


# is operator: identity operator  in membership operator
firstName = "Titan"
secondName = "AOT"
lastName = "Titan"

fruits = ["apples", "mangoes", "tomatoes","pineapples"]

output = firstName is secondName
output = firstName is lastName
output = 'i' in lastName
output = "apples" in fruits

#Example Two
my_str ="Hello World!"
output = "He" in my_str # True
print("l" in my_str)#True
print("y" in my_str)#False
    

# ternary operator: <return statement> if <condition> else <return statement>
output = "AOT !!!" if secondName == "AOT" else "Titan"

targetFruit ="green apple"
availableFruit ="green apple"
alternative = "pineapples"

# simple conditinal statement
if targetFruit ==  availableFruit:
    output = "Take green apples!"
else:
    output = "Take pineapples or any cirtic fruit"

 #Example 2
if lastName == "AOT":
    output = "AOT !!!"
else:
    output = "Titan"
   

#  ternary operator
output = "Take green apples!" if targetFruit ==  availableFruit else "Take pineapples or any cirtic fruit"

"""
Data Types: 
    - boolean: stores either True or False
    - number [ int, float, complex]
    - Strings
    - lists
    - tuples
    - dictionaries
    - set
ENUMS

"""
"""
 precede it with is..
"""

isOpen = True # boolean
isLoading = False # boolean
 
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
print("================================================")
print(output)
print("================================================")


#if else conditional statements and elif condition with comparison operators
#example 
age = 20

if age>=18:
    output = "You are an adult"
else:
    output ="You are not an adult yet"
print(output)
print("========================================")
#Example 2
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant



"""
conditional statements with logical operators 
"""

#without boolean operator
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

# with and operator

is_citizen = True
age = 20

if is_citizen and age >= 18:
    print("You are eligible to vote")

else :
    print("You not are eligible to vote")

    """
    In the example above, is_citizen is True, and age >= 18 evaluates to True. Since both operands of the and operator are truthy, the condition is_citizen and age >= 18 evaluates to True, and the print call in the if block is executed.
    """

# with or operator
Age = 22
IsWorking = False
print(Age or IsWorking)#22
#eg 2
Age = 19
IsStudent = True

if age < 18 or IsStudent:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

    """
    In this case, age < 18 is False, but is_student is True. Since at least one condition is true, the entire or expression evaluates to True, and the discount message in the if block is printed.
    """

# not operator - used to check if something is not True or False 

is_student = False

if not is_student:
    print("Not eligible for a bursary")
else: 
    print("You are eligible for a bursary")