#Find the area and circumference of circle.

#taking radius as input

radius  = float(input("Enter the radius of the circle: "))

pi = 3.1416

#calculating area

area = pi * radius**2

#calculating circumference

circumference  = 2 * pi * radius

print("The area of the circle is: ", area)

print("The circumference of the circle is: ", circumference)