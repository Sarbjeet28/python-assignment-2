#16  Write a Python program to create a symmetric difference and set difference
A = {'a', 'b', 'c', 'd','e','f','g'}
B = {'c', 'd', 'e' }

# returns all items to result variable except the items common in both sets
result = A.symmetric_difference(B)
print(result)

