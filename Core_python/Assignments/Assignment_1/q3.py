#Program to find quotient and remainder of two numbers.


#input two number from user

num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))


#calculate the quotient

quotient = num1 // num2

#calculate the remainder 

remainder = num1 % num2

print("The quotient is: ", quotient)
print("The remainder is: ", remainder)