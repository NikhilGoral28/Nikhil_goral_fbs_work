#Write a program to check if entered year is a leap year or not


def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Year is leap"
    else:
        return "year is not leap"

year  = int(input("Enter a year: "))

leap = is_leap(year)
print(leap)