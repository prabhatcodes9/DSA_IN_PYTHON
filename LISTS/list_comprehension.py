prev_list = [1,2,3,4]
new_list = [i*2 for i in prev_list]
print(prev_list)
print(new_list)

language = "Python"
new_list = [letter for letter in language]
print(new_list)

# Conditional list comprehension
lu_list = [-1, 10, -20, 2, -99, 88, 20]
new_list = [number**2 for number in lu_list if number<0]
print(new_list)

po_list = [number if number > 0 else 0 for number in lu_list]
print(po_list)