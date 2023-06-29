# Given a list of numbers, return the maximum value.
import heapq
# def max_value(nums):
  # heapq.nlargest(2, range(len(nums), key=nums.__getitem__))
  
def max_value(nums):
  max1 =  max(nums)
  # max2 = max(nums -1)
  return nums.index(max1)


  
 

# Test cases
print(max_value([4, 7, 2, 8, 10, 9]))
print(max_value([-5, -2, -1, -11]))