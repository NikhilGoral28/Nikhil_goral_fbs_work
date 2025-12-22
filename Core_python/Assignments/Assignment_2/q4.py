#WAP to calculate area of triangle and rectangle

rect = input("Enter length and breadth of rectangle separated by comma: ")
length, breadth = rect.split(",")

triangle = input("Enter base and height of triangle separated by comma: ")
base, height = triangle.split(",")

#area of rectangle
area_rectangle = int(length) *  int(breadth)
#area of triangle
area_triangle = 0.5 * int(base) * int(height)
print("Area of rectangle is:", area_rectangle)
print("Area of triangle is:", area_triangle)