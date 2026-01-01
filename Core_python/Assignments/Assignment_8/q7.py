#Write a program to find sum of digits of a number.

def sum_of_digit(num):
    
    total = 0
    while num > 0:
        digit = num % 10
        num = num//10

        total += digit

    return total


num = int(input("Enter a number: "))
sum_of_digit = sum_of_digit(num)

print(f"Sum of the digit of the given number {sum_of_digit}")