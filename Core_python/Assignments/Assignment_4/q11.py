#WAP to check if given number Strong Number. 


num = int(input("Enter a number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    sum = sum + fact
    num = num // 10

if sum == temp:
    print(f"{temp} is a strong number.")
else:
    print(f"{temp} is not a strong number.")