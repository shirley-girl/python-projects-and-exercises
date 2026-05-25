# single comment

"""
multi-line comment
"""


"""

======= VARIABLE =======
- containers that store ref so something in memory
- parts: 
    - variable name
    - assignment operator(=)
    - value

=== RULES ===
- name in accordance to what it is eg firstName = "John" and not x = "John
- do not start the naming with a number or a special character eg $, %,e.t.c
- do not use inbuilt key-words eg def, and, or, if, while ,do e.t.c
- either name your variables via camelCase(firstName) or snake_case(first_name)
"""

firstName = "John"
secondName = "Doe"
# lastName = input("Enter last name: ") # standard output

# standard output
# print("Hello ", firstName, lastName)


"""
FUNCTION: 
- does something
- parameterized
- non- parameterized
- fuunction can return something 
- parts: 
    - keyword: def
    - function name
    - parethesis+colon: ():
    - the contents must be equally indented by 4-space

=== RULES ===
 - must have indentation
 - key word + function name, parenthesi + colon must be present
 - naming must either be camel case or snake case
 - must only serve one purpose #singleResponsibility
 - when you define a function, to use it make sure you call the function

"""

# DEFINEd a non-parameterized function
def greeting():
    print("Hellow Dunia!!")

#  CALL-ing the function
greeting()

# DEFINed a parametriezd function
def morningGreeting(name):
    print("Good morning", name)

# CALLing the function:
morningGreeting("Mary Johnes")

def afternoonGreetings(name):
    return "Good Afternoon! " + name

greetings = afternoonGreetings(name="Wonder Woman")

print(greetings)

def morningGreet(name):
    print("My name is", name)

morningGreet("Ann Moraa")


# Apply diacount function
def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    elif not isinstance(discount,(int, float)):
        return "The discount should be a number"

    elif price <= 0:
        return "The price should be greater than 0"

    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    else:
        discount_amount =(discount*price)/100
        final_price = price - discount_amount
        return final_price

final_price = apply_discount(60, 10) 
print(final_price)