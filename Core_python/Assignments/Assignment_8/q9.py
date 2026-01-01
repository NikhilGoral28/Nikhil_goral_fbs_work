#Write a program to check if entered number is a palindrome or not.




def is_palindrome(num):

    reverse = 0

    while num > 0:
        digit = num % 10
        num = num // 10

        reverse = digit + reverse * 10

    
    if num == reverse:
        return "Number is palidrome"
    else: 
        return "Not a palindrome"

num = int(input("Enter a number: "))

palindrome= is_palindrome(num)

print(palindrome)