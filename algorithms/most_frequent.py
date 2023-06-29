# Given a string, return the most frequent character within that string.

def most_frequent_char(string):      
  result = max(string, key = lambda letter : string.count(letter))  
  return result

# Test cases
print(most_frequent_char('bookeeper')) # -> 'e'
print(most_frequent_char('david')) # -> 'd'
print(most_frequent_char('bittersweet'))