# Tuples
# Implement a function that takes a tuple of strings as input and returns a new tuple 
# containing only the strings that start with an uppercase letter.

def filter_uppercase_strings(strings):
    # Your code here
    result = []
    # print(strings[0][0].isupper())
    for string in strings:
        if string[0].isupper():
            result.append(string)
    return tuple(result) 

# Test the function
strings = ("Apple", "banana", "Cat", "dog", "Elephant", "Frog")
print(filter_uppercase_strings(strings))  
# Expected output: ("Apple", "Cat", "Elephant")
