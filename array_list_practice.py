# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements

myList = [1,2,3,4]

def middle(lst):
    return lst[1:-1]
print(middle(myList))

# Given 2D list calculate the sum of diagonal elements.

myList2D = [[1,2,3],[4,5,6],[7,8,9]]
def diagonal_sum(matrix):
    total = 0 
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total
print(diagonal_sum(myList2D))

# Given a list, write a function to get first, second best scores from the list.

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
def first_second(my_list):
    first = second = float('-inf')
    for num in my_list:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return first , second
print(first_second(myList))

# Write a function to remove the duplicate numbers on given integer array/list

array = [1,1,2,3,4,5]
new = []
def remove_duplicates(arr):
    for i in arr:
        if i not in new:
            new.append(i)
remove_duplicates(array)
print(new)

# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs

myList = [2,4,3,5,6,-2,4,7,8,9]
def pair_sum(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(f"{myList[i]}+{myList[j]}")
    return result
print(pair_sum(myList, 7))

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums = [1,2,3,1]
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(contains_duplicate(nums))

# Permutation

mylist1 = [1,2,3,4]
mylist2 = [2,1,4,3]
def permutation(mylist1, mylist2):
    if len(mylist1) != len(mylist2):
        return False
    mylist1.sort()
    mylist2.sort()
    if mylist1 == mylist2:
        return True
    else:
        return False
print(permutation(mylist1, mylist2))

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly

matrix = [[1,2,3],[4,5,6],[7,8,9]]
def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
print(rotate(matrix))
