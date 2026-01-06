#Write a program to reverse a given number using recursive function.


def reverse(num,rev=0):

    if num == 0:
        return rev
    
    return reverse(num // 10 , rev*10 + num%10)


n = int(input("Enter Number: "))
print(reverse(n))