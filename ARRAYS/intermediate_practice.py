from array import *

# 1. Second Largest Element

arr = array('i', [12,35,1,10,34,1])
first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print("Second largest element is: ", second)

# 2. Remove duplicates from array

arr1 = [1,2,2,3,4,4,5]
unique = []
for num in arr1:
    if num not in unique:
        unique.append(num)
print(unique)

# 3. Rotate the array by k positions

arr2 = [1,2,3,4,5]
k = 2
n = len(arr2)
k = k % n 
rotated = arr2[-k:] + arr2[:-k]
print(rotated)

# 4. Check if array is Palindrome

arr3 = [1,2,3,2,1]
if arr3 == arr3[::-1]:
    print("Yes")
else:
    print("No")

# 5. Find Pairs with Given Sum

arr4 = [1,5,7,-1,5]
target = 6
for i in range (len(arr4)):
    for j in range(i+1, len(arr4)):
        if arr4[i] + arr4[j] == target:
            print(f"Pair : ({[i]}, {[j]})")

# 6. Find missing number (1 to n)

arr5 = [1,2,4,6,3,7,8]
n = 8
expected_sum = n * (n+1) // 2
actual_sum = sum(arr5)
missing = expected_sum - actual_sum
print("Missing number: ", missing)

# 7. Count Frequency without Dictionary

arr6 = [4,5,4,5,4]
n = len(arr6)
visited = [False]*n

for i in range(n):
    if visited[i]:
        continue
    count = 1
    for j in range(i+1, n):
        if arr6[i] == arr6[j]:
            count +=1
            visited[j] = True
    print(f"{arr6[i]} - {count} times(s)")