#Write a program to enter P, T, R and calculate simple Interest


#enter the principal amount, time and rate of interest from user

p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in years: "))
r = float(input("Enter the rate of interest: "))


#calculate the simple interest

si = (p * t * r) / 100
print("The simple interest is:", si)