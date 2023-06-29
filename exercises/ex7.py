# Sets
# Implement a function that takes two sets of integers as input and returns 
# a new set containing the INTERSECTION of the two sets.

def find_intersection(set1, set2):
    # Your code here
        result = set1.intersection(set2)
        return result
       
# Test the function
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(find_intersection(set1, set2))  
# Expected output: {4, 5}

# Intersection: Elements two sets have in common.

# ----------------------------------------------------------------------------------------------------------


# Implement a function that takes two sets of integers as input and returns a new set containing 
# the UNIQUE elements from both sets.

def merge_sets(set1, set2):
    # Your code here
    uniques = set1.union(set2)
    return uniques

# Test the function
print(merge_sets(set1, set2))  
# Expected output: {1, 2, 3, 4, 5, 6, 7, 8}


# Union: All the elements from both sets. Uniques because sets only have unique values