# Lists 
# Implement a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.

def sum_even_numbers(numbers):
    # Your code here
    total=0
    for x in numbers:
        if x%2==0: 
            total=total+x
    return total      

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(numbers))  # Expected output: 30
