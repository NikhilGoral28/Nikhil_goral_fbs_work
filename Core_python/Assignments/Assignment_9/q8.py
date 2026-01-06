#Write a program to check whether a number is prime or not using recursion


def CheckPrime(n,i =2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    

    return CheckPrime(n,i+1)


num = int(input("Enter number: "))

if CheckPrime(num):
    print("Number is prime")

else:
    print("Number is not prime")