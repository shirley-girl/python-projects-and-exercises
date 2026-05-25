# Dictionaries
"""
dictionaries are built-in data structures that store collections of key-value pairs


- Dictionaries store data as key-value pairs inside {}
- Keys are used to access values
- Keys must be unique and immutable (e.g., string, int, tuple)
- Values can be any data type and can repeat
- Each pair is separated by a comma
"""
# Example
Pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}


# looping over a dictionary - to access or process  it's key - value pairs 
""" This is helpful for updating their values or applying some logic to them """

products = {
    "laptop" : 990 ,
    "Smartphone": 600,
    "Tablet": 250,
    "Headphones": 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8) # updating the price by applying a 20% discount on all products

print(products)

print("============================================================")

# general loop examples on dictionary

for price in products.values():
    print(price)

print("============================================================")
for product in products.keys():
    print(product)

print("============================================================")
for product in products.items():
    print(product)

print("============================================================")
for product, price in products.items():
    print(product, price)


# Enumerate() function
