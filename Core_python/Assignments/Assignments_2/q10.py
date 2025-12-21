#write a program to reverse three-digit number. 


num = int(input("Enter three-digit number: "))

if len(str(num)) ==3:
    unit_digit = num %10
    second_digit = (num % 100)//10

    hun_digit = num //100

    reverse_num = unit_digit * 100 + second_digit *10 + hun_digit
    print(reverse_num)
else:
    print("pls,Enter three digit number")


#for any length of number

num = int(input("Enter a number: "))

rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print("Reversed Number is:", rev)