#1
digits = [1,2,3]
def plusOne(digits):
    num = int(''.join(map(str, digits)))
    result = num + 1
    digit_list = [int(d) for d in str(result)]
    print(digit_list)
plusOne(digits)

#2
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)
nums = [1,3,5,6]
print(searchInsert(nums, 2))