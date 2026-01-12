#Write a program to remove all occurrences of a given element in the list.

lst = list(map(int,input("Enter a list: ").split()))
num = int(input("Enter a number: "))


l = [i for i in lst if i != num]

print(l)