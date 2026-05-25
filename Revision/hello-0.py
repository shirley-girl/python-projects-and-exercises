# single line comment

"""
multi-line comment
"""

"""
VARIABLE: 
- container that stores ref to something
- type inferencing
- Scopes (Global & Local )

==== Rules ====
- name it in accordance to what it is eg person name => name= "Jne Does, but not x = "John Doe"
- do not use inbuilt keywords/ primitives eg if, when, match, while, and, or etc
- do not start it with special characters or number eg 123... , %...
- name it either using camelcase(firstName) or snakecase(first_name)

"""

firstName = "Jane" # global vairable
lastName = "Jules" # global variable


# standard Input
# secondName = input("Kindly enter secondName: ") 

# # standard output
# print("================================================")
# print(firstName,lastName, sep=" <===> " )
# print(firstName,lastName, sep=" <****> ")
# print(firstName,lastName, secondName, sep=" <****> ")
# print("================================================")

"""
FUNCTIONS:
- a group/ block of code that does something
- parameterized and non parameterized functions
- functions can return a value

==== RULES ====
- must have the keyword def
- name of the function must be able to explain itself( name it in accordance to what it does)
- add a parenthesis () followed by a colon :
- the function precedures should be indented with 4 spaces (press tab)

"""

# defined a function 
def greetings(): 
    print("Hello World!")

# call the function
# greetings()
 
#  parameterized function
def morningGreeting(name):
    print("Good morning", name)

# call the function
# morningGreeting(name="Juliet")    

#  function definition
def updateFirstName():
    firstName = input("Enter new name: ")
    middleName = "Kong" # local variable
    print(firstName,middleName, lastName)


#  call function
# updateFirstName()
# print(firstName)


