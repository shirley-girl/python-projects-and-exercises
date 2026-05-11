"""
1. for loops - used to run a block of codes a set number of time
"""
#eg 1
Fruits = ["pineapple", "apple", "pears", "mango", "stawberries"]

for Fruit in Fruits:
    print(Fruit)

# LOOPS IN STRING
for char in "fruit":
    print(char)

# Nested loops
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

# eg 2 - use of break statement
developer_names = ["Naomi","Ann","John","Doe","Joanne",]

for developer in developer_names:
   # developer = input("Enter developer's name: ")
    if developer == "Joanne":
        break
  #  print(developer)

#eg 3 continue statement in for loop
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer) #statement skips the second iteration of the loop when developer is equal to Naomi, and does not print that name to the terminal, the other two names are printed to the terminal

"""
while loop - this repeats a code of block until the condition is false
"""
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')



"""
List Comprehension

List comprehension allows one to create a new list in a single line by combining a loop and condition directly within square brackets. This makes the code shorter and often easier to read.
"""

# eg 1. without list comprehension
even_numbers = []

for num in  range (25):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

#eg 2 with list comprehension

even_numbers = [num for num in range(25) if num %2 == 0 ]
print(even_numbers)


numbers = [2,3,4,5,6]
result = [(number, "even") if number % 2 == 0 else (number,"odd") for number in numbers]
print(result)

# filter() function 
"""
- Used to filter elements from an iterable based on a condition. It returns an iterator that contains only the elements that satisfy the condition. 

Here is an example of creating a new list of just words longer than four characters:
"""

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

# Map () function
"""
used to
"""