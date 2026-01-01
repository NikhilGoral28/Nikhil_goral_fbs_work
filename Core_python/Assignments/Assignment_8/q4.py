#Sum of all odd numbers between 1 to n  


def sum_of_odd():
    n = int(input("Enter n: "))

    total = 0

    for i in range(1,n+1):
        if i % 2 != 0:
            total += i
    
    return total


a = sum_of_odd()
print(f'sum of odd upto n is {a}')