#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ").strip().lower()

if (gender == "male" and age >= 21 ) or (gender == "female" and age >= 18):
    print("You are eligible to marry.")
else:
    print("You are not eligible to marry.")
    