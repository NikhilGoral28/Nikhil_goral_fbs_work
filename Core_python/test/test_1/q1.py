length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")

radius = input("Enter the radius of the circle: ")

area_rect = int(length) * int(width)
area_circle = 3.14 * int(radius) * int(radius)

print("Area of Diagram:", area_rect+(area_circle/2))