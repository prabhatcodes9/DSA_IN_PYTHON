my_List = [10,20,30,40,50,60,70,80,90]
target = 90
if target in my_List:
    print(f"{target} in list")
else:
    print(f"{target} not in list")

# Linear search

my_List1 = [10,20,30,40,50,60,70,80,90]
def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1
    
print(linear_search(my_List1, target))