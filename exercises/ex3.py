# Exercise 3: Loops
# TODO: Write code that prints all between 1 and n using a while loop
# TODO: Write code that prints all the even numbers between 1 and n using a for loop

def main(n):
    print("All numbers from 1 to n:")
    # use a while loop
    i=0
    while i < n :
     i= i+1
     print(i)


    print("Even numbers between 1 and n:")
    # even numbers from 1-20 (for loop)
    for num in range(2, n+1, 2):
        print(num)

# Other solution: 
    # for y in range(1, n):
    #      if y%2 == 0:
    #       print(y)
         
        


main(12)