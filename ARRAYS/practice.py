# def max_product(arr):
#     max1, max2 = 0, 0
#     for i in arr:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif i > max2:
#             max2 = i
#     return max1, max2
# arr = [1,7,3,4,9,5]
# print(max_product(arr))

digits = [1,2,3]
def plusOne(digits):
    for i in range(len(digits)):
        return i+1
print(plusOne(digits))

