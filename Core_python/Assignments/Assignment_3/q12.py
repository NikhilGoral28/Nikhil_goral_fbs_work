#Write a program to check if given 3 digit number is a palindrome or not

num = int(input("Enter a 3-digit number: "))
if 100 <= num <= 999:
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10

    if hundreds == units:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")