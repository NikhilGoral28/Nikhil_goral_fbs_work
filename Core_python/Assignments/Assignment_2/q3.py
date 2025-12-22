#Convert distant given in feet and inches into meter and centimeter


distanace = input("Enter distance in feet and inches format: ")

feet, inches = distanace.split(",")

#conversion formula

meters = int(feet) * 0.3048 + int(inches) * 0.0254
centimeters = meters * 100

print("Distance in meters is:", meters)
print("Distance in centimeters is:", centimeters)