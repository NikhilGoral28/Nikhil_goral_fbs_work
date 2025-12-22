#Program to Find the Roots of a Quadratic Equation

#taking input from user

a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

#calculating the discriminant 

d = b**2 - 4*a*c

#calculating the two roots
if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("The roots are real and different.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif d == 0:
    root = -b / (2*a)
    print("The roots are real and the same.")
    print("Root:", root)
else:
    realPart = -b / (2*a)
    imagPart = (-d**0.5) / (2*a)
    print("The roots are complex and different.")
    print("Root 1: {} + {}i".format(realPart, imagPart))
    print("Root 2: {} - {}i".format(realPart, imagPart))