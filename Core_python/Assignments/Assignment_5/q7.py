"""Write a program to solve the following series :  
a. 1! + 2! + 3! + 4! + .....n!  
b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)  
c. Find the sum of a geometric series from 1 to n where the common ratio is 2.  
d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10  
e. x - x2/3 + x3/5 - x4/7 + .... to n terms  """


n = int(input("Enter the value of n: "))

# a. 1! + 2! + 3! + 4! + .....n!
factorial_sum = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    factorial_sum += factorial
print("Sum of factorials up to", n, "is:", factorial_sum)

# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
exponent_sum = 0
for i in range(1, n + 1):
    exponent_sum += n ** i
print("Sum of series N + N^2 + ... + N^N is:", exponent_sum)

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
geometric_sum = 0
for i in range(n):
    geometric_sum += 2 ** i
print("Sum of geometric series up to", n, "terms is:", geometric_sum)