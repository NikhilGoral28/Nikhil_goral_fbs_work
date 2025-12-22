#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = float(input("Enter first side of the triangle: "))
side2 = float(input("Enter second side of the triangle: "))
side3 = float(input("Enter third side of the triangle: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("Entered sides do not form a valid triangle.")