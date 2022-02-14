# Python code to swap two numbers
# without using another variable


x = 5
y = 7

print("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# code to swap 'x' and 'y'
x, y = y, x

print("After swapping: ")
print("Value of x : ", x, " and y : ", y)

print("###########################################################")


# Python code to swap two numbers
# using + and - operators


x = 5.4
y = 10.3

print("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# Swap code
x = x + y  # x = 15.7, y = 10.3
y = x - y  # x = 15.7, y = 5.4
x = x - y  # x = 10.3, y = 5.4

print("After swapping: ")
print("Value of x : ", x, " and y : ", y)
