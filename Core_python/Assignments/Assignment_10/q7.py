#Write a program to create a new list from existing list which contains cube of each number of list


lst = list(map(int, input("Enter a list: ").split()))


CubeList = []


for i in lst:
    CubeList.append(i**3)

print("cube list of the existing list: ",CubeList)