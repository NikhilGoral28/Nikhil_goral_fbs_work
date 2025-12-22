#WAP to calculate selling price of book based on cost price and discount.


cost_price = float(input("Enter cost price of the book: "))

discount_percent = float(input("Enter discount percentage: "))

#calculation of selling price

discount_amount = (cost_price * discount_percent)/100

print("Selling price of the book is: ", (cost_price - discount_amount))