#Write a program to find factorial using recursion.


def Fact(n):
    if n == 0:
        return 1
    
    else:
        return n * Fact(n-1)
    

n = int(input("Enter a number: "))
print(Fact(5))