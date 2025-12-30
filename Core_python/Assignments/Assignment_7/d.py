n = 5
for i in range(1, n + 1):
   
    for j in range(n - i):
        print(" ", end=" ")

    
    for j in range(i, i + i):
        print(j, end=" ")

    
    for j in range(i + i - 2, i - 1, -1):
        print(j, end=" ")

    print()


