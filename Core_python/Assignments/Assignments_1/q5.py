#Write a program to enter P, T, R and calculate Compound Interest.


#Accept the principal amount, time and rate of interest

p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in year: "))
r = float(input("Enter the rate of interest: "))

#calculate the compount interest

amount = p * (pow((1 + r / 100), t))
ci = amount - p

print("The compound interest is:", ci)