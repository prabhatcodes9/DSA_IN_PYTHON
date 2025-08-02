import numpy as np

twoDArray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(twoDArray)

# 1. Insertion in Two Dimensional array

# inserting column

newTwoDArray = np.insert(twoDArray, 4, [[1,2,3,4]], axis=1)
print(newTwoDArray)

# inserting row

newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=0)
print(newTwoDArray)

# we can use append to insert row or columns at end

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)

# 2. Access an element of Two Dimensional Array

print(twoDArray[0][3])
print(twoDArray[1][2])

# using def

def accessElement(array, rowindex, columnindex):
    if rowindex >= len(array) or columnindex >= len(array[0]):
        print("Error!")
    else:
        print(array[rowindex][columnindex])
accessElement(twoDArray, 2, 3)

# 3. Traversing Two Dimensional Array

def traverse(array):
    for i in range (len(array)):
        for j in range (len(array[0])):
            print(array[i][j])
traverse(twoDArray)

# 4. Searching Two Dimensional Array

def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return "The value is located at index " + str(i) + " "+ str(j)
    return "Error!"
print(search(twoDArray, 14))

# 5. Deletion in 2D array

new = np.delete(twoDArray, 0, axis=1)
print(new)
