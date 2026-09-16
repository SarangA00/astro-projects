import math

# Factorial calculator
def factorial(n):
    if (n == 0 or n == 1): # Base Case
        return 1
    else:
        return n * factorial(n-1) # Recursive Case

# Test cases
print(factorial(0))
print(factorial(1))
print(factorial(5))


# Recursive sum on vel data
vel_list = [4.25, 10.36, 11.19, 5.03, 60.2]
def recursive_sum(nums):
    if nums == []:
        return 0
    else:
        return nums[0] + recursive_sum(nums[1:])

print(recursive_sum(vel_list))