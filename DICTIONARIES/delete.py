# Using del method
myDict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
del myDict['age']
print(myDict)

# Using pop method
my_Dict = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
removed_element = my_Dict.pop('age', None)
print(removed_element)
print(my_Dict)

# Using pop item 
my_Dict1 = {'name':'Prabhat', 'age':18, 'address':'India', 'language':'Python'}
removed_element = my_Dict.popitem()
print(removed_element)
print(my_Dict)

# Using clear method to remove all element from dictionary
