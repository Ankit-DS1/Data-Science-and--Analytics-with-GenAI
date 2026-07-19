                                #Dictionary 

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# It is defined by curly braces {} and key-value pairs are separated by a colon :. 
# Dictionaries are mutable, meaning you can change their content after creation.
# Keys must be hashable (immutable), while values can be of any data type.
# Dictionaries do not allow duplicate keys, but they can have duplicate values.

#1. Creating a dictionary

my_dict = {
    "name": "Ankit",
    "age": 24,
}

my_dict["age"] = 23

print(my_dict)
print(my_dict["name"])

# Dictionary constructor

d = dict(name="Ankit", age=24, city="Patna")
print(d)

d = dict([("name", "Ankit"), ("age", 24), ("city", "Patna")])
print(d)


#Dictionary Trasversing

my_dict = {
    "name": "Ankit",
    "age": 24,
    "city": "Patna"
}

for i in my_dict.values():
    print(i) #prints keys
    print(my_dict[i]) #prints values

#Dictionary Methods
my_dict = {
    "name": "Ankit",
    "age": 24,
    "city": "Patna"
}

del my_dict["city"] #Removing a key-value pair
print(my_dict)

my_dict.clear() #Removing all key-value pairs
print(my_dict)

my_dict.items() 
print(my_dict)


