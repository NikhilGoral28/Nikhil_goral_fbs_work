#Write a program to remove duplicates from the list. 


lst  = list(map(int, input("Enter a list: ").split()))

Ulist = []

for i in lst:
    if i not in Ulist:
        Ulist.append(i)

print("unique Element lis : ", Ulist)