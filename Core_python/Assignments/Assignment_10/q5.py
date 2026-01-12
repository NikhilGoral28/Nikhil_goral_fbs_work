# Accept a number from user and check if this element is present in the list or 
#not. Also tell how many times it is present in the list.

lst = list(map(int, input('Enter a list: ').split()))

num = int(input("Enter a number: "))

count = 0

for i in lst:
    if i == num:
        count += 1
        


if count > 0:
    print(f"element found {count} times.")
else:
    print("Element not found")