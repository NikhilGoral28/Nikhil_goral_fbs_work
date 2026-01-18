#Python Program to Put Even and Odd elements of a List into two Different List

l = list(map(int,input("Enter a list: ").split()))


odd = []
even =[]


for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


print("odd elements are: ", odd)
print("Even elements are: ", even )