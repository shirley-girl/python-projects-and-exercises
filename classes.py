"""
- Are build to define shared behaviours of object, the objects that use then behaviours are then created
- i.e classes are like footprint or template used to create objects

How classes are created:
 - use keyword class
 - followed by the name of the class
 - then a colon




A class can contain:
 - Attributes → variables that store data
 - Methods → functions that define behavior

Syntax:
 class ClassName:
     def __init__(self, ...):
         self.attribute = value

     def method(self):
        pass
"""

class ClassName:
    def __init__(self, name, age): #is a special method automatically called when a new object is created. It initializes the attributes of the objects that will be created with the class.
        self.name = name
        self.age = age

    def sample_method(self):               
        print(self.name.upper())
    
# example 2
"""
2 containing objects created from the class and calling the methods
"""

# defining class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof!, I'm {self.age} years old")
#  Create objects (instances)
dog_1 = Dog ("Jack", 2)
dog_2 = Dog("Thatcher",5)

# call method
dog_1.bark()
dog_2.bark()


# Attributes
# difference between class attributes and instance attributes

# Example 1
class Dog:
    species = "French Bulldog" # Class attribute

    def __init__(self, name):
        self.name = name # Instance attribute

print(Dog.species) # French Bulldog

dog1 = Dog("Jack")
print(dog1.name)    # Jack
print(dog1.species) # French Bulldog

dog2 = Dog("Tom")
print(dog2.name)    # Tom
print(dog2.species) # French Bulldog

# example 2 with a method
class Dog:
   species = "French Bulldog"

   def __init__(self, name):
     self.name = name

   def bark(self):
       return f"{self.name} says woof woof!"

jack = Dog("Jack")
jill = Dog("Jill")

print(jack.bark()) # Jack says woof woof!
print(jill.bark()) # Jill says woof woof!

# example 3
class Cars:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def describe(self):
        print(f"This is a {self.color}, {self.model} car!")
# create car objects
car_1 = Cars("red", "Toyota Corolla")
car_2 = Cars("green", "Lamborghini Revuelto")

print(car_1.describe())
print(car_2.describe())


# Handling object Attributes Dynamically
"""
"""
# built in functions that dynamically work with object attributes

"""
1. getattr() - used to access/read attributes from objects when you don't know it's name until runtime.
"""
# example 1
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30) 
 
print(getattr(person, 'name')) # John Doe 
print(getattr(person, 'age')) # 30 
print(getattr(person, 'city', 'Milano')) # Milano

# eaxample 2
class Person:
    def __init__(self, name, age):
        self.name
        self.age

person = Person('Shirley May', 32)

attr_name = int("Enter the name you want to see : ")
print(getattr(person, attr_name, 'Attribute not found'))


"""
2. dir(obj) - lists all the attributes of an object
- callable() → checks if attribute is a method
- attr.startswith('__') → filters out special (dunder) methods

"""
# here is an example

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)

# Loop through all attributes of the person object with dir() function
for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(person, attr)): 
        value = getattr(person, attr)
        print(f'{attr}: {value}')

# Output
# age: 30
# name: John Doe

"""
3. setattr() 
- This function lets you create a new attribute or update an existing one dynamically. The syntax looks like this:

setattr(object, attribute_name, value) 
"""

# example

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30

"""
4. hasattr()
- It checks if an attribute exists and returns True or False based on the result.

Here's the basic syntax:

hasattr(object, attribute_name)  
"""
# example
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        # Access the attributes dynamically once their existence is confirmed
        print(f'{attr}: {getattr(product_a, attr)}')

# Output:
# name: T-Shirt
# price: 25
# ERROR: Product is missing the required attribute: 'inventory_id'

"""
5. delattr()
- The delattr() lets you remove an attribute dynamically:
The basic syntax looks like this:

delattr(object, attribute_name) 
"""

# eaxmple




# MUSICAL INSTRUMENT INVENTORY - classes and calling methods

class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())

instrument_2.play()
print(instrument_2.get_fact())



# Planet Class
"""
User Stories:

You should create a class named Planet.
The Planet class should have an __init__ method that:
Has four parameters: self, name, planet_type, and star.
Raises a TypeError with the message name, planet type, and star must be strings if any of the arguments passed in is not a string type.
Raises a ValueError with the message name, planet_type, and star must be non-empty strings if any of the arguments passed in is an empty string.
Assigns the values passed in to the instance attributes name, planet_type, and star.
The Planet class should have an orbit method that returns a string in the format {name} is orbiting around {star}....
The Planet class should have a __str__ method that returns a string in the format Planet: {name} | Type: {planet_type} | Star: {star}.
You should create three instances of the Planet class named planet_1, planet_2, and planet_3.
You should print each planet object to see the __str__ method output.
You should call the orbit method on each planet object and print the result.

"""
class Planet:

    def __init__(self, name, planet_type, star):
        
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        
        
        if name.strip() == "" or planet_type.strip() == "" or star.strip() == "": 
            raise ValueError('name, planet_type, and star must be non-empty strings')

        self.name = name
        self.planet_type = planet_type
        self.star = star

    
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


planet_1 = Planet("Earth", "Terestrial", "sun")
planet_2 = Planet("Mars", "Terestrial", "sun" )
planet_3 = Planet("Jupiter", "Gas Giant", "Sun")

print(planet_1)

print(planet_2)

print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

