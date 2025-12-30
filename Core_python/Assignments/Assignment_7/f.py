n = 5

for i in range(1, n + 1):
    print(i, end=" ")
print()


for i in range(2, n + 1):
    
    print(i, end=" ")

    for j in range(2 * (n - i) - 1):
        print("", end=" ")
        
    
    if i != n:
        print(n)
    else:
        print()
