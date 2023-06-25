# Given a list of numbers, return the maximum value.

def max_value(nums):
  nums.sort()
  return(nums[-1])

# Test cases
# print(max_value([4, 7, 2, 8, 10, 9]))
print(max_value([-5, -2, -1, -11]))