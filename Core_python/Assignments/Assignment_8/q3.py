"""
Write a program to find sum of following series using functions : 
a.   1+ 2 + 3 + 4+..... + n 
b.  1!+ 2! + 3! + 4!+..... + n! 
c.  1^1 + 2^2 + 3^3+ ...... n^n  """




def series_sum(n):

    #1+ 2 + 3 + 4+..... + n
    total = 0
    for i in range(n+1):
        total += i
 
    print("1+ 2 + 3 + 4+..... + n", total)
    
    # 1!+ 2! + 3! + 4!+..... + n!  
    factsum= 0
    fact = 1
    for i in range(1,n+1):
        fact *= i

        factsum += fact
    
    print("1!+ 2! + 3! + 4!+..... + n!",factsum)

    
    #1^1 + 2^2 + 3^3+ ...... n^n

    powSum = 0

    for i in range(n+1):
        powSum += pow(i,i)

    print("1^1 + 2^2 + 3^3+ ...... n^n",powSum)



n = int(input("Enter n: "))
series_sum(n)