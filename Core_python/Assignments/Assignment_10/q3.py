#Write a program to find the second largest element in the list


lst = list(map(int,input("Enter the list: ").split()))


high = lst[0]
secodhigh = lst[0]

for i in range(1,len(lst)):
    if lst[i] > high:
        secodhigh = high
        high = lst[i]
    
    elif lst[i] < high and lst[i] > secodhigh:
        secodhigh = lst[i]


print(f"Second highest element is {secodhigh}")