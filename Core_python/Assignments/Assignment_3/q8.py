"""Write a program to prompt user to enter userid and password. After verifying 
userid and password display a 4 digit random number and ask user to enter the 
same. If user enters the same number then show him success message otherwise 
failed. (Something like captcha) """

import random

correct_userid = "admin"
password  = "password123"

entered_userid = input("Enter userid: ")
entered_password = input("Enter password: ")

if entered_userid == correct_userid and entered_password == password:
    captcha  = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_input = int(input("Enter the captcha number displayed above: "))
    if user_input == captcha:
        print("Success!")
    else:
        print("Failed! Invalid captcha entered.") 
else:
    print("Invalid userid or password.")