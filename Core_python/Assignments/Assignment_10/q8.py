#  Write a program to create a duplicate of an existing list. It should not point to same list

lst = list(map(int, input("Enter a list: ").split()))

duplicate = [i for i in lst]

print("duplicate list:",duplicate)