# 1. update the list

myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
print(myList)

# 2. insert a value

# at beginning
myList.insert(0,11)
print(myList)

# at any position
myList.insert(3,99)
print(myList)

# at end
myList.append(100)
print(myList)

# add another list to list
newList = [22,33,44,66,88]
myList.extend(newList)
print(myList)