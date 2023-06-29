# Write a function that checks whether a given number num is a prime number.
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
#
# RETURNS a boolean

def is_prime_number(num):
     # TODO: Check if num is a prime number
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i)==0:
                return False      
        else:
            return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
is_prime = is_prime_number(num)
print(is_prime)
if is_prime:
    print(num, "is a prime number.")
else: 
    print(num, "is not a prime number.")
    


