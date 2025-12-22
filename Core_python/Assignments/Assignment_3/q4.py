#Write a program to input all sides of a triangle and check whether triangle is valid or not.


side1 = float(input("Enter first side of the triangle: "))
side2 = float(input("Enter second side of the triangle: "))
side3 = float(input("Enter third side of the triangle: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The triangle is valid.")
else:
    print("Entered sides do not form a valid triangle.")