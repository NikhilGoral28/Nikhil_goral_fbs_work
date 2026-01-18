#Python Program to Find the Union of two Lists


lst1 = [10,20,30,40,50]

lst2 = [40,50,60,70,80,90]


union_lst = lst1.copy()

for item in lst2:
    if item not in union_lst:
        union_lst.append(item)


print("Union list: ", union_lst)