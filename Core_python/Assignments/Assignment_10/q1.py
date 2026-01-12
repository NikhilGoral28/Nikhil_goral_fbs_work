# Write a program to find sum of all elements of list


lst = list(map(int,input("Enter a list of numbers by sep ,: ").split(',')))


total = 0

for i in lst:
    total += i

print(f"sum of the list is {total}")