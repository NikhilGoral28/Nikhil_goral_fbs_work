#Write a program to find sum of n numbers using recursion

def sumSeries(n):
    if n == 0:
        return 0
    return n + sumSeries(n-1)


n = int(input("Enter number: "))

print(sumSeries(n))