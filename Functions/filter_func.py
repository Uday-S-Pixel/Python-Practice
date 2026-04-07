# syntax
# filter(function, iterable)
# used to filter iterables using a function

print("Enter a list of numbers")
num_lst = list(map(int, input().split()))

def check_even(x):
  if x % 2 == 0:
   return True
  else: 
   return False
even_num = list(filter(check_even, num_lst))# check_even being the function to filter the list

def check_odd(x):
 if x % 2 != 0:
  return True
 else:
  return False
odd_num = list(filter(check_odd, num_lst ))

print(f"The list you entered is {num_lst}")
print(f"The even numbers in the list are {even_num}")
print(f"The odd numbers in the list are {odd_num}")
