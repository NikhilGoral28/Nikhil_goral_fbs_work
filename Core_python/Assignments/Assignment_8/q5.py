#Sum of all prime numbers between 1 to n 



def sum_of_prime(n):


    total = 0

    for num in range(2,n+1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total += num
            
        
    return total


n = int(input('Enter a number: '))
total = sum_of_prime(n)
print(f"Sum of the prime numbers upto {n} is {total}")