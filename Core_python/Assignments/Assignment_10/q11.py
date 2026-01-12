#Write a program to print all numbers which are divisible by m and n in the list. 

lst = list(map(int, input("Enter list: ").split()))

m = int(input("Enter m: "))
n = int(input("Enter n: "))


for num in lst:
    if num % m == 0 and num % n == 0:
        print(num)