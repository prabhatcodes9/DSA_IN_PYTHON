# FIND THE LARGEST NUMBER
array = [3,7,1,9,4]
def largest(array):
    for i in range (0, len(array)):
        return max(array)
print(largest(array))

# FIND THE SMALLEST NUMBER
array1 = [12,5,8,19,2]
def smallest(array):
    for i in range(0, len(array)):
        return min(array)
print(smallest(array1))

# SUM OF ALL ELEMENTS
array2 = [1,2,3,4,5]
def SumElements(array):
    for i in range(0, len(array)):
        return sum(array)
print(SumElements(array2))

# REVERSE A LIST
list = [1,2,3,4]
def reverse(list):
    for i in range(0, len(list)):
        return list[::-1]
print(reverse(list))

# CHECK IF LIST IS SORTED
list1 = [1,2,3,4,5]
def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True
print(is_sorted(list1))

# COUNT OCCURRENCES OF AN ELEMENT
arr = [1,2,2,3,2]
def count_element(array, element):
    occur = 0
    for i in range(0, len(array)):
        if array[i] == element:
            occur += 1
    return occur
print(count_element(arr, 2))

# REMOVE DUPLICATES
list0 = [1,2,2,3,4,4,5]
def remove_duplicates(list):
    new = []
    for i in list0:
        if i not in new:
            new.append(i)
    return new
print(remove_duplicates(list0))

# FIND SECOND LARGEST ELEMENT
arr1 = [10,20,4,45,99]
def second_largest(arr1):
    first = second = float('-inf')
    for i in arr1:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
    return second
print(second_largest(arr1))

# ROTATE LIST BY K STEPS
arr2 = [1,2,3,4,5]
def rotate_list(arr2, k):
    n = len(arr2)
    for i in arr2:
        k = k % n
        rotated = arr2[-k:] + arr2[:-k]
    return rotated
print(rotate_list(arr2, 2))

# PAIR SUM PROBLEM
arr3 = [1,2,3,4,5]
def pair_sum(arr3, target):
    pairs = []
    for i in range(0, len(arr3)):
        for j in range(i+1, len(arr3)):
            if arr3[i] + arr3[j] == target:
                pairs.append((arr3[i], arr3[j]))
    return pairs
print(pair_sum(arr3, 6))

# Count the frequency of each element in a list using a dictionary.
input = [1,2,2,3,1,4]
def count_frequency(input):
    count = {}
    for i in input:
        count[i] = count.get(i, 0) + 1
    return count
print(count_frequency(input))

# FIND KEY BY VALUE
d = {'a':10, 'b':20, 'c':10}
def find_key(d, value):
    return [k for k, v in d.items() if v == value]
print(find_key(d, 10))

# MERGE TWO DICTIONARIES
d1 = {'a':1}
d2 = {'b':2}
def merge(d1,d2):
    merged = d1.copy()
    merged.update(d2)
    return merged
print(merge(d1,d2))

# SWAP KEYS AND VALUES
input0 = {'a':1, 'b':2, 'c':3}
def reverse_key(input0):
    return {v:k for k, v in input0.items()} 
print(reverse_key(input0))

# CHECK IF KEY EXISTS
d = {'x':100, 'y':200}
def key_exists(d, key):
    return key in d
print(key_exists(d, 'y'))

# MAX VALUE KEY
dd = {'a':5, 'b':10, 'c':8}
def max_value_key(dd):
    return max(dd, key=dd.get)
print(max_value_key(dd))

# SUM OF ALL VALUES 
ddd = {'x':1, 'y':2, 'z':3}
def sum_values(ddd):
    return sum(ddd.values())
print(sum_values(ddd))

# REMOVE KEY
D = {'x':1, 'y':2}
def remove_key(D, key):
    D.pop(key, None)
    return D
print(remove_key(D, 'y'))

# DICTIONARY OF SQUARES

       
