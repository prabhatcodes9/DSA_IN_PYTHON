# SEARCH FOR AN ELEMENT

myDict = {'name':'Prabhat', 'age':18, 'address':'India'}
def searchElement(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'Error!'
print(searchElement(myDict, 18))

# Time complexity : O(n)
# Space complexity : O(1 )