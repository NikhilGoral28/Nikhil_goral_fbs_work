#Write a program to calculate area of circle

def area(r):

    pi = 3.14
    area = pi*r**2

    return area


r = int(input("Enter a Radius of circle: "))
area = area(r)
print(f"Area of circle is {area}")
