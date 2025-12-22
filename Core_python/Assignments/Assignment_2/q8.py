#Write a program to swap two numbers using third variable


num1 = input("Enter first number: ")
num2 = input("ENter second number: ")

temp = num1
num1 = num2
num2 = temp

print("Swapped 1st number:", num1)
print("Swappped 2nd number:",num2)