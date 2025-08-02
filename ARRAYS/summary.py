from array import *

# 1. Create an array and tranverse.

arr1 = array('i', [1,2,3,4,5,6])
def tranverse(array):
    for i in array:
        print(i)
tranverse(arr1)

# 2. Access individual elements through indexes

def accessElements(array, index):
    if index >= len(array):
        print("Error!")
    else:
        print(array[index])
accessElements(arr1, 5)

# 3. Append any value to the array using append() method

arr2 = array('i', [1,2,3,4,5])
arr2.append(6)
print(arr2)

# 4. Insert value in an array using insert() method

arr3 = array('i', [100,200,300,400])
arr3.insert(3,600)
print(arr3)

# 5. Extend python array using extend() method

arr4 = array('i', [10,11,12])
arr1.extend(arr4)
print(arr1)

# 6. Add items from list into array using fromlist() method

l = [20,21,22]
arr4.fromlist(l)
print(arr4)

# 7. Remove an array element using remove() method

arr5 = array('i', [10,20,30,40,50])
arr5.remove(40)
print(arr5)

# 8 . Remove last array element using pop() method

arr6 = array('i', [21,22,23,24,25])
arr6.pop(4)
print(arr6)

# 9. Fetch any element through its index using index() method

arr7 = array('i', [19,29,39,49,59])
def accessElements(array, index):
    if index >= len(array):
        print("Error!")
    else:
        print(array[index])
accessElements(arr7, 3)

# 10. Reverse a python array using reverse() method

arr8 = array('i', [11,22,33,44,55])
arr8.reverse()
print(arr8)

# 11. Get array buffer information through buffer_info() method

arr9 = array('i', [1,2,3,4,5,6,7,11,14,23])
print(arr9.buffer_info())

# 12. Check for number of occurences of an element using count() method

arr10 = array('i', [1,5,1,6,9,11,43,1,7,1])
print(arr10.count(1))

# 13. Convert array to string using tostring() method

str = arr1.tobytes()
print(str)


# 14. Convert array to a python list with same elements using tolist() method

list = arr1.tolist()
print(list)

# 15. Append a string to char array using fromstring() method

ints = array('i')
ints.frombytes(str)
print(ints)

# 16. Slice Elements from an array

print(arr10[0::2])