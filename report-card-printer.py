name = 'Alice'
print(name)
print(name, type(name))

is_student = True
print(is_student, type(is_student))#The print() function can display more than one value at a time. Separate values with a comma (,) to print them on the same line.
age=20
print(age,type(age))

score=(80.5)
print(isinstance(score, int))# results shows false because the value in score is a float number and not integer
print(score, type(score))











#isinstance is used to check whether a variable belongs to a specific data type eg : handling user input safely

#age = input("Enter age: ")

if isinstance(age, str):
    age = int(age)

#print(age + 5)
   
   #OR

x = "two"

if isinstance(x, int):
    print("x is an integer")
else:
    print("x is not an integer")


#len()  function

"""
len() function is used determine the length of a string and working with individual character of a string(Indexing)"""

   #Example
FirstName = "Janet"
print(len(FirstName))#5

"""
To access a character by its index, you use square brackets ([]) with the index of the character you want to access inside."""
       # Example:
print(FirstName[2]) # 'n' third character
print(FirstName[0]) # 'J' First character
print(FirstName[-1]) # 'e' Negative indexing, this is the second last character


"""Strings are immutable data types in Python. This means that you can reassign a different string to a variable:"""

    #example
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
   #But direct modification of a string isn't allowed:

#greeting = 'hi'
#greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

#String Concatenation

my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 +" " + my_str_2
print(str_plus_str) # Hello World


name= "John Doe"
age = 26
output = name + str(age)
print(output)