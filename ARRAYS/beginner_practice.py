from array import *

# 1. Print first and last element

arr = array('i', [10,20,30,40,50])
print(arr[0], arr[4])

# 2. Traverse

arr1 = array('i', [1,2,3,4,5])
def traverse(array):
    for i in array:
        print(i)
traverse(arr1)

# 3. Sum of all elements

arr2 = array('i', [5,10,15,20])
total = sum(arr2)
print(total)

# 4. Find maximum in elemrnt

arr3 = array('i', [11,25,7,34,19])
print(max(arr3))

# 5. Reverse the array

arr4 = array('i', [1,2,3,4])
arr4.reverse()
print(arr4)

# 6. Search of an element

arr5 = array('i', [3,8,15,10])
def search(array, element):
    if element in array:
        print("Found")
    else:
        print("Error!")
search(arr5, 15)

# 7. Remove an Element

arr6 = [1,10,3,10,5]
def remove(array, element):
    if element in array:
        while element in array: # as multiple instances of element exist, and i want to remove all of them, so i use while loop
            array.remove(element)
    else:
        print("Element not found")
remove(arr6, 10)
print(arr6) 

# 8. Count even and odd numbers

arr7 = [1,2,3,4,5,6,7]
even = 0
odd = 0
for num in arr7:
    if num%2 == 0:
        even +=1
    else:
        odd +=1
print("Even: ", even)
print("Odd: ", odd)

# 9. Calculate average of array

arr8 = [10,20,30,40,50]
average = sum(arr8)/len(arr8)
print(average)

# 10. Frequency of each element

arr9 = array('i', [1,2,2,3,1,4,2])
print(arr9.count(1))
print(arr9.count(2))