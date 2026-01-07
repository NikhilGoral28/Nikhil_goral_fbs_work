""". Write a program to check if given number is Armstrong number or not.  
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +  
4*4*4*4) """

num = int(input("Enter a number: "))

temp = num 
sum = 0

# count number of digits
n = len(str(num))
while num > 0:
    digit = num % 10
    sum = sum + digit ** n
    num = num // 10
    
if sum == temp:
    print(f"{temp} is an Armstrong number.")
else:
    print("number is not armstrong number")