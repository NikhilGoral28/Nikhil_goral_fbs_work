#Python Program to Sort the List According to the Second Element in Sublist

lst = [[1, 3], [4, 1], [2, 2], [5, 0]]


sorted_lst = sorted(lst, key=lambda x: x[1])

print("Sorted list:", sorted_lst)