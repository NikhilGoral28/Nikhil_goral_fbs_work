""" Accept age of five people and also per person ticket amount and then calculate total 
amount to ticket to travel for all of them based on following condition : 
a. Children below 12 = 30% discount 
b. Senior citizen (above 59) = 50% discount 
c. Others need to pay full"""


# Person 1
age1 = int(input("Enter age of person 1: "))
ticket1 = float(input("Enter ticket amount for person 1: "))

# Person 2
age2 = int(input("Enter age of person 2: "))
ticket2 = float(input("Enter ticket amount for person 2: "))

# Person 3
age3 = int(input("Enter age of person 3: "))
ticket3 = float(input("Enter ticket amount for person 3: "))

# Person 4
age4 = int(input("Enter age of person 4: "))
ticket4 = float(input("Enter ticket amount for person 4: "))

# Person 5
age5 = int(input("Enter age of person 5: "))
ticket5 = float(input("Enter ticket amount for person 5: "))


# Person 1
if age1 < 12:
    discount1 = 0.30 * ticket1
elif age1 > 59:
    discount1 = 0.50 * ticket1
else:
    discount1 = 0.0
final1 = ticket1 - discount1

# Person 2
if age2 < 12:
    discount2 = 0.30 * ticket2
elif age2 > 59:
    discount2 = 0.50 * ticket2
else:
    discount2 = 0.0
final2 = ticket2 - discount2

# Person 3
if age3 < 12:
    discount3 = 0.30 * ticket3
elif age3 > 59:
    discount3 = 0.50 * ticket3
else:
    discount3 = 0.0
final3 = ticket3 - discount3

# Person 4
if age4 < 12:
    discount4 = 0.30 * ticket4
elif age4 > 59:
    discount4 = 0.50 * ticket4
else:
    discount4 = 0.0
final4 = ticket4 - discount4

# Person 5
if age5 < 12:
    discount5 = 0.30 * ticket5
elif age5 > 59:
    discount5 = 0.50 * ticket5
else:
    discount5 = 0.0
final5 = ticket5 - discount5


print(f"Amount to pay for person 1: {final1}")
print(f"Amount to pay for person 2: {final2}")
print(f"Amount to pay for person 3: {final3}")
print(f"Amount to pay for person 4: {final4}")
print(f"Amount to pay for person 5: {final5}")

total_amount = final1 + final2 + final3 + final4 + final5
print(f"Total amount to pay for all 5 people: {total_amount}")
