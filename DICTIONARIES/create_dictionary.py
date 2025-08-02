# Using dict constructor
my_dict = dict(one = "uno", two = "dos", three = "tres")
print(my_dict)

# Using curly brackets
my_dict1 = {
    "one" : "uno",
    "two" : "dos",
    "three" : "tres"
}
print(my_dict1)

# Using list of tuples

my_list_of_tuples = [("one", "uno"), ("two", "dos"), ("three", "tres")]
my_dict2 = dict(my_list_of_tuples)
print(my_dict2)