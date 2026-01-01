#Write a program find reverse of a number


def reverse(num):

    reverse = 0

    while num > 0:
        digit = num % 10
        num = num // 10

        reverse = digit + reverse * 10

    return reverse

num = int(input("Enter a number: "))
reverse = reverse(num)

print(reverse)