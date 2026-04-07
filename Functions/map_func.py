# syntax
# map(function, iterable)

print("Enter a list of numbers")
num_lst = list(map(int, input().split()))

'''
 we use the keyword list to convert the data into a list
 map() is used so that we convert the input (string) into integers
 input() is used to take input from the user
 split() is used so that the input which is given is split by spaces
'''
print(f"Your list is {num_lst}")

def square(x):
  return x  ** 2
sq_lst = list(map(square, num_lst))
print(f"The squares are {sq_lst}")

cube_lst = list(map(lambda x: x ** 3, num_lst))# printing cube of the numbers using lambda functionṇṇ
print(f"The cubes are {cube_lst}")
