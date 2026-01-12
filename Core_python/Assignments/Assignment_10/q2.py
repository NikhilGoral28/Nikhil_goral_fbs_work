#Write a program to find maximum and minimum element in a list

lst = list(map(int, input("Enter a list: ").split()))


max = lst[0]

min = lst[0]

for i in range(1,len(lst)):
    if lst[i] > max:
        max = lst[i]

    if lst[i] < min:
        min = lst[i]


print(f"maximum element is {max}")
print(f"Minimum element is {min}")
    