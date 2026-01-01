# WAP to check if a given number is Armstrong number or not. For each task create separate functions. 
 

def count_digits(num):
    return len(str(num))


def is_armstrong(num):
    n = count_digits(num)
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10
    return total == num


def main():
    number = int(input("Enter a number: "))
    if is_armstrong(number):
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")


main()

 
 
 
