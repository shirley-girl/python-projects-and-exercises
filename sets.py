# SETS - are built-in python data structures
"""   
         characteristics

 - Sets don't store duplicate values. If you try to add a duplicate value to a set, only one of them will be stored.
 - Sets are mutable and unordered (no indexing)
 - Elements must be immutable (e.g., int, str, tuple)
 - Support set operations: union, intersection, difference, symmetric difference
 - sets are defined by writing it's elements with curly braces, separated with commas

"""
# example
my_set = {1, 2, 3, 4, 5}

# defining empty sets - by use of set() function
set() # set
{} # will define a dictionary


# addition 
my_set.add(6)
print(my_set)

# adding an element that's already in a set will only keep one item 
my_set.add(5) 
print(my_set)


# issubset () and issuperset() methods
"""
They check if a set is a subset or superset of another set, respectively.
"""

# example
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 5}

print(your_set.issubset(my_set)) # True
print(my_set.issuperset(your_set)) # True


# isdisjoint() methods -
# example
my_set = {1, 2, 3}
your_set = {4, 5, 6}

print(my_set.isdisjoint(your_set)) # True