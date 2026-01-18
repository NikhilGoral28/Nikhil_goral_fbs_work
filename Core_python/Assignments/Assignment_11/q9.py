#Write a program to create three lists of numbers, their squares and cubes


num  = list(range(1,11))

square = [x**2 for x in num]

cubes = [x**3 for x in num]


print('Numbers: ', num)
print("Squares: ", square)
print("Cubes: ", cubes)

