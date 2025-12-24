#WAP to print all numbers in a range divisible by a given number.


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

div = int(input("Enter the divisor: "))

for num in range(start, end + 1):
    if num % div == 0:
        print(num)