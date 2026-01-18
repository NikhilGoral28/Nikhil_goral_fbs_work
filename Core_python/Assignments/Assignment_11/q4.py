#Python Program to Find the Second Largest Number in a List Using Bubble Sort 


lst = [12,45,4,54,31,10]


n = len(lst)


for i in range(n):
    for j in range(0,n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1],lst[j]



second_el = lst[-2]


print["Sorted list: ", lst]
print("Second largest element: ", second_el)