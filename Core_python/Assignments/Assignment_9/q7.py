#Write a program to find sum of digits using recursion.



def sumDigit(n):
    if n == 0:
        return 0
    
    digit = n %10
    return digit +sumDigit(n//10)


n = int(input("Enter number: "))

print(sumDigit(n))