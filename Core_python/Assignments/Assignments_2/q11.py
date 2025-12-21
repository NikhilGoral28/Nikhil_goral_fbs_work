#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.


amount = int(input("Enter the amount: "))


notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

count = 0

while amount > 0:
    for note in notes:
        if amount >= note:
            amount -= note
            count += 1
            break
print("Minimum number of notes needed:", count)
