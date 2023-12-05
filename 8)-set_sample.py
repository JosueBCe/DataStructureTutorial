# Set Samples 

""" In this example will look at how to work with a list and 
delete the duplicates using set(). """

my_list = [0, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

no_duplicates = set(my_list)

print(no_duplicates)

""" Let's say that we need to make a function 
that deletes the value from the set. For learning purposes, we will 
check first if the value is in the set and then delete it. """


def delete_value(value):
    # using hashing to check if the value is in the set
    if value in no_duplicates:
        # removing the value from the set
        no_duplicates.remove(value)

delete_value(1)
print(no_duplicates) # Expected output { 0, 2, 3, 4, 5, 6, 7, 8, 9, 10 }

