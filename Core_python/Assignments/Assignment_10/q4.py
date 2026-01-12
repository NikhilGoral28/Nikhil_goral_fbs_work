#Write a program to reverse the list


#ls= list(map(int,input("Enter a list: ").split()))

lst  = [12,3,4,4,54,32,21]
rev= []

for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])

print(rev)