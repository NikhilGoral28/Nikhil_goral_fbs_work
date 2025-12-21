#Write a program to convert days into years, weeks and days.

#taking input from user
total_days = int(input("Enter the number of days: "))

#calculating years, weeks and days

years = total_days // 365
remaining_days = total_days % 365

weeks = remaining_days // 7
days = remaining_days % 7
print("Years:", years)
print("Weeks:", weeks)