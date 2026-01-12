#Write a program to print list after removing even numbers. 
 


lst = list(map(int,input("Enter a list: ").split()))

l = [i for i in lst if i % 2 != 0]

print(l)