# using print function and f'string for debbuging
def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result
print(add(2,3))

# using python built-in pdb for interactive debugging

import pdb

def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2))

# using vs debugging tools

def divide(a, b):
    result = a / b
    return result

print(divide(10, 2))
print(divide(15, 3))


# Using Raise Statement

def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative