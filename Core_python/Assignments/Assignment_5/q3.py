"""
Accept no. of passengers from user and per ticket cost. Then accept age of each  
 
passenger and then calculate total amount to ticket to travel for all of them based on  
following condition :  
a. Children below 12 = 30% discount  
b. Senior citizen (above 59) = 50% discount  
c. Others need to pay full"""

num_passengers = int(input("Enter number of passengers: "))

for i in range(num_passengers):
    age = int(input(f"Enter age of passenger {i + 1}: "))
    ticket_cost = float(input(f"Enter ticket cost for passenger {i + 1}: "))

    if age < 12:
        discount = 0.30
    elif age > 59:
        discount = 0.50
    else:
        discount = 0.0

    total_cost = ticket_cost * (1 - discount)
    print(f"Total cost for passenger {i + 1} is: {total_cost:.2f}")

