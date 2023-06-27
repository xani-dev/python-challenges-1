# Write a function that generates the Fibonacci sequence up to a given number n.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
# starting with 0 and 1.
#
# RETURNS an int

def generate_fib(n):
    # TODO: Generate the Fibonacci sequence up to n
     if n < 0:
          print('Incorrect Input')
     elif n == 0:
          return [0]
     elif n == 1:
          return [0,1]
     else:
        fib_sequence = [0,1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            return fib_sequence

   
# Test the function with the following code
n = int(input("Enter the number: "))
fib_sequence = generate_fib(n)
print("Fibonacci sequence up to", n, ":", fib_sequence)

