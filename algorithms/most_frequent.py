# Given a string, return the most frequent character within that string.

def most_frequent_char(s):
  char_counter={}
  for letter in s:
    if letter in char_counter:
      char_counter[letter]+=1
    else:
      char_counter[letter]=1
      max_count=0
      letter=''
      for letter, count in char_counter.items():
        if max_count < count:
          max_count = count
          char = letter
          return char
        
  

# Test cases
print(most_frequent_char('bookeeper')) # -> 'e'
# print(most_frequent_char('david')) # -> 'd'