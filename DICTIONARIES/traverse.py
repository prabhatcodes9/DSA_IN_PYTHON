myDict = {'name':'Prabhat', 'age':18, 'address':'India'}
def traverse(dict):
    for key in dict:
        print(key, dict[key])
traverse(myDict)  # Time complexity : O(n)
                  # Space complexity : O(1)