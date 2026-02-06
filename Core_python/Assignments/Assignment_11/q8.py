#Print 1 to 100 in snakes and ladder pattern. 

n = 10

count = 100

for i in range(n):
    row = []

    for j in range(n):
        row.append(count)

        count -= 1

    
    if i % 2  == 1:
        row.reverse()
    
    print(ro)