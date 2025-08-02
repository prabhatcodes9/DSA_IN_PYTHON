# Copy method

my_Dict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
dict = my_Dict.copy()
print(my_Dict)
print(dict)

# fromkeys method

my_Dict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
newDict = {}.fromkeys([1,2,3], 'Prabhat')
print(newDict)

# get method

my_Dict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
print(my_Dict.get('city'))

# items method

my_Dict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
print(my_Dict.items())

# keys method

my_Dict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
print(my_Dict.keys())

# setdefault method

my_Dict1 = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
default = my_Dict1.setdefault('age1', 20)
print(default)
print(my_Dict1)

# values method

my_Dict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
print(my_Dict.values())

# update method

my_Dict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
newDict1 = {"one" : "uno",
    "two" : "dos",
    "three" : "tres"}
my_Dict.update(newDict1)
print(my_Dict)