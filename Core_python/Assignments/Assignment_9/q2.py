#Write a program to check if given number is Armstrong or not using recursive function


def CheckArmstrong(n, power):
    if n == 0:
        return 0
    digit = n % 10

    return (digit ** power) + CheckArmstrong(n // 10, power)

num = int(input("Enter Number: "))
pow = len(str(num))

if CheckArmstrong(num,pow) == num:
    print("Number is Armstrong number")
else:
    print("Number is not armstrong")

