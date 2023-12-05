""" Let's practice using this new data structure 
Are you sure you want to do this? 👟🎧
"""


def union(set1, set2):
    """ TODO: complete this function to 
    unify the values of the 2 sets (don't use the union built-in function)""" 
    pass

def intersection(set1, set2):
    """ TODO: complete this function to find the intersection 
    between the two sets (don't use the intersection built-in function) """
    pass

def what_is_different(set1, set2):
    """ TODO: complete this function to find the difference between the set1 and set2
    (don't use the difference built-in function) """

A = {1, 2, 3}
B = {3, 4, 5}


print(union(A, B)) # Expected output { 1, 2, 3, 4, 5 }

print(intersection(A, B)) # Expected output { 3 }

print(what_is_different(A,B)) # Expected output { 1, 2 }