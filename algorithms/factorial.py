# Write a function to calculate the factorial of a given number (n).
# hint: try recursion

def factorial(n):
   if n==1 or n==0:
      return 1
   else:
      return (n*factorial(n-1))

# Test case
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")

