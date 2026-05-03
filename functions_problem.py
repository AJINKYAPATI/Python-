# Write a function to find maximum of three numbers in Python.

def maximum_num (val1,val2,val3):
    if val1 > val2 and val1>val3:
        print(val1,"is the maximum number")
    elif val2 > val1 and val2 > val3:
        print(val2,"is the maximum number")
    else:
        print(val3,"is the maximum number")
maximum_num(12,34,56)



# Write a Python function to create and print a list where the
# values are square of numbers between 1 and 30.
def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)

        return l
    print(create_list())


# Write a Python function that takes a number as a parameter
# and check if the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(17))



# Write a Python function to sum all the numbers in a list.
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total            
numbers = [12, 4, 5, 6, 7, 8, 9]
print(sum_list(numbers))
 




# Write a Python program to solve the Fibonacci Sequence
# using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
