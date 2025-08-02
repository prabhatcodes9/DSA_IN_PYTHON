# Using in 

newTuple = ('a', 'b', 'c', 'd', 'e')

print('a' in newTuple) # Time complexity : O(n)

# Index method

print(newTuple.index('a')) # Time complexity : O(n)

# Custom method

def searchElement(p, element):
    for i in range(0, len(p)):
        if p[i] == element:
            return f"The {element} is found at {i} index"
    return 'Error'

print(searchElement(newTuple, 'b')) # Time complexity : O(n) # Space Complexity : O(1)

