"""  
      1  
    1   1 
  1   2    1
1   3    3   1    """


rows = 4

for i in range(rows):
    print("  " * (rows - i - 1), end="")
    for j in range(i + 1):
        print(1 if j == 0 or j == i else i, end="   ")
    print()
