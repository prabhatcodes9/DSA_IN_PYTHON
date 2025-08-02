init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
print(result)

# Write a function that calculates the sum and product of all elements in a tuple of numbers.

def sum_product(t):
    sum_result = 0
    product_result = 1
 
    for num in t:
        sum_result += num
        product_result *= num
 
    return sum_result, product_result
 
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)

# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
def tuple_elementwise_sum(tuple1, tuple2):
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return result
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)

# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

input_tuple = (2, 3, 4)
value_to_insert = (1)
def insert_value_front(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)

# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

input_tuple = ('Hello', 'World', 'from', 'Python')
def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)
output_string = concatenate_strings(input_tuple)
print(output_string)

# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))
output_tuple = get_diagonal(input_tuple)
print(output_tuple)

# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)