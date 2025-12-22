#Write a program to check if user has entered correct userid and password


correct_userid = "admin"
correct_password = "password123"

entered_userid = input("Enter userid: ")
entered_password = input("Enter password: ")

if entered_userid == correct_userid and entered_password == correct_password:
    print("Login successful.")
else:
    print("Invalid userid or password.")