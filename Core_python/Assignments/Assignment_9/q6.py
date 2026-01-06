#Write a program to print Fibonacci series using recursion. 


def fab(n):

    if n == 0:
        return 0
    if n ==1:
        return 1


    return fab(n-1) + fab(n-2)



n  = int(input("Enter number: "))
for i in range(n):
    print(fab(i), end=" ")