#12 . Write a program to create three lists of numbers, their squares and cubes 



lst = list(map(int,input("Enter a number: ").split()))
 
square = [i**2 for i in lst]

cube = [i**3 for i in lst]

print(lst)
print(square)
print(cube)