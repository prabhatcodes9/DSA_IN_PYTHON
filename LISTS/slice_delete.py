# 1. Slicing

myList = ["a", "b", "c", "d", "e", "f"]
print(myList[0:3])

# 2. Deletion

myList1 = ["a", "b", "c", "d", "e", "f"]
myList1.pop(1)
print(myList1)

myList2 = ["a", "b", "c", "d", "e", "f"]
del myList2[0:2]
print(myList2)

myList3 = ["a", "b", "c", "d", "e", "f"]
myList3.remove("e")
print(myList3)

