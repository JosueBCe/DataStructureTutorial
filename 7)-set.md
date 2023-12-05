# Set {}

A set is a collection of unique elements with certain characteristics:
- It does not allow duplicates.
- The elements are not sorted.
- It is not guaranteed to be filled in all the spaces.
- It uses hashing to enable adding, removing, and testing for membership in constant time (O(1)).

Set has various uses, including:
- Finding unique values, such as in a list.
- Providing quick access to previously calculated unique results.

## Set operations
To work with sets in Python:
- To define an empty set, use `set()`.
- To define a set with elements, use curly braces `{}`.
- Adding a value: `my_set.add(value)`.
- Removing a value: `my_set.remove(value)`.
- Checking if a value is in the set: `if value in my_set:`.
- Getting the size: `length = len(my_set)`.

## Other operations (Math operations)
Sets in mathematics have several operations that can be performed on them:

1. Union: The union of two sets A and B, denoted by A ∪ B, is the set that contains all the elements present in A or B or both.
   ````python
   A = {1, 2, 3}
   B = {3, 4, 5}
   union_set = A.union(B)
   print(union_set)  # Output: {1, 2, 3, 4, 5}
   ```

2. Intersection: The intersection of two sets A and B, denoted by A ∩ B, is the set that contains all the elements present in both A and B.
   ````python
   A = {1, 2, 3}
   B = {3, 4, 5}
   intersection_set = A.intersection(B)
   print(intersection_set)  # Output: {3}
   ```

3. Difference: The difference of two sets A and B, denoted by A - B, is the set that contains all the elements present in A but not in B.
   ````python
   A = {1, 2, 3}
   B = {3, 4, 5}
   difference_set = A.difference(B)
   print(difference_set)  # Output: {1, 2}
   ```

4. Symmetric Difference: The symmetric difference of two sets A and B, denoted by A △ B, is the set that contains all the elements present in either A or B, but not in both.
   ````python
   A = {1, 2, 3}
   B = {3, 4, 5}
   symmetric_difference_set = A.symmetric_difference(B)
   print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
   ```

5. Subset and Superset: A set A is a subset of another set B, denoted by A ⊆ B, if all the elements of A are also present in B. If A is a subset of B and B is not equal to A, then B is called a superset of A, denoted by B ⊇ A.
   ````python
   A = {1, 2}
   B = {1, 2, 3}
   print(A.issubset(B))  # Output: True
   print(B.issuperset(A))  # Output: True
   ```