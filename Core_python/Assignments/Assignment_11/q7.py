#Python Program to Find the Intersection of Two Lists


lst1 = [10,20,30,40,50]

lst2 = [40,50,60,70,80,90]


intersection_lst = []

for item in lst1:

    if item in lst2:
        intersection_lst.append(item)


print("Intersection of two list: ",  intersection_lst)