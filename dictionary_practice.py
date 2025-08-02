# Define a function to count the frequency of words in a given list of words.

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
print(count_word_frequency(words))

# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
print(merge_dicts(dict1, dict2))

# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary

my_dict = {'a': 5, 'b': 9, 'c': 2}

def max_value_key(my_dict):
    return max(my_dict, key = my_dict.get)
print(max_value_key(my_dict))

# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

my_dict = {'a': 1, 'b': 2, 'c': 3}
def reverse_dict(my_dict):
    return {v:k for k , v in my_dict.items()}
print(reverse_dict(my_dict))

# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
def filter_dict(my_dict, condition):
    return {k: v for k , v in my_dict.items() if condition(k,v)}
print(filter_dict(my_dict, lambda k,v:v%2 == 0))

# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
    
def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)
print(check_same_frequency(list1, list2))          

