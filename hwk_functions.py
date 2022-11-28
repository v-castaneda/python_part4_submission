# Write a Python function called max_num()to 
# find the maximum of three numbers.
def max_num(a, b, c):
    return  max([a, b, c])

print('Problem 1')
print(max_num(2, 0, 8))
print(max_num(-5, -3, -18))
print(max_num(2, 0, -100))

# Write a Python function called mult_list() 
# to multiply all the numbers in a list.
def mult_list(num_list):
    product = 1
    for num in num_list:
        product = product * num
    return product

print('Problem 2')
print(mult_list([1, 3, 5]))
print(mult_list([0, 4, 10]))
print(mult_list([-4, -8, -2]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(my_string):
    return my_string[::-1]

print('Problem 3')
print(rev_string('Victor'))
print(rev_string('Hello World'))

# Write a Python function called num_within() to check whether 
# a number falls in a given range. The function accepts the number, 
# beginning of range, and end of range (inclusive) as arguments.
# Examples: 
# num_within(3,2,4) returns True, 
# num_within(3,1,3) returns True, 
# num_within(10,2,5) returns False.
def num_within(num, range_low, range_high):
    if num >= range_low and num <= range_high:
        return True
    else:
        return False

print('Problem 4')
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# Write a Python function called pascal() that 
# prints out the first n rows of Pascal's triangle.

# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
