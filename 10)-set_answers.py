""" Let's practice using this new data structure 
"""


def union(set1, set2):
    """ TODO: complete this function to 
    unify the values of the 2 sets (don't use the union built-in function)""" 

    for value in set1: set2.add(value)

    return set2

def intersection(set1, set2):
    """ TODO: complete this function to find the intersection 
    between the two sets (don't use the intersection built-in function) """
    intersection = set()

    for item in set2:
        if item in set1:
          
            intersection.add(item)

    return intersection

def what_is_different(set1, set2):
    """ TODO: complete this function to find the difference between the set1 and set2
    (don't use the difference built-in function) """
    difference = set()
    for item in set1:
        if item not in set2:
            difference.add(item)
    return difference

A = {1, 2, 3}
B = {3, 4, 5}

print(union(A, B)) # Expected output { 1, 2, 3, 4, 5 }

C = { 1, 2, 3, 4, 5}
D = {3, 4, 5}

print(intersection(C, D)) # Expected output { 3, 4 ,5 }

print(what_is_different(C,D)) # Expected output { 1, 2 }

def factorial(n):
	if n <= 1:
		return 1  # 1! = 1 (no recursion)
	else:
		return n * factorial(n-1)  
     
