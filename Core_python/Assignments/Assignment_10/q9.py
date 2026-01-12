'''
Write a program of having n number of elements in the list and find out even 
and odd elements in that list and then create two separate lists which will have 
even elements and other will have odd elements. 
'''

lst = list(map(int,input("Enter a list: ").split()))

odd = []
even = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even list: ",even)
print("odd list: ", odd)