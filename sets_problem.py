# Write a program to find max and min in a set.I
a= {12, 34, 56, 78, 90, 1, 57}
maximum = max(a)
minimum = min(a)
print ("The minimum value in the set is :", minimum)
print ("The maximum value in the set is :", maximum)

# Write a program to find common elements in
# three lists using sets.
a = [1,5,6,8,2]
b = [4,5,6,7]
c = [1,9,6,2,5]
print("The common elements in the three lists are: ", set(a) & set(b) & set(c))

# Write a program to find difference between two sets.
a = {1,5,6,8,2}
b = {1,9,6,2,5}

print (b.difference(a))

# Write a Python program to remove an item from
# a set if it is present in the set.
a = {1,5,6,8,2}
a.discard(5)
print(a)
 

# Write a Python program to check if a set
# is a subset of another set.
a = {1,2,3,4,5,6}
b = {2,3,4}
print(b.issubset(a))


