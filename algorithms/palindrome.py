# Write a function that takes a string as input and checks if it is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward,
# disregarding spaces, punctuation, and capitalization.
#
# RETURNS a boolean
import re
def is_palindrome(text):
    # TODO: Check if text is a palindrome
    text_to_check = re.sub('\W+','', text.upper())
    text1= text_to_check
    text2 = text_to_check[::-1]
    if text1 == text2:
        return True
    else:
        return False
    

# Test the function
text = input("Enter a string: ")
is_palindrome = is_palindrome(text)
if is_palindrome:
    print(text, "is a palindrome.")
else:
    print(text, "is not a palindrome.")
