"""
 
1. Write a program to prompt user to enter userid and password. If Id and  
 
password is incorrect give him chance to re-enter the credentials. Let him try 3  
times. After that program to terminate. """


userid = "admin"
password = "admin@123"

for i in range(3):
    user_input_id = input("Enter User ID: ")
    user_input_password = input("Enter Password: ")
    
    if user_input_id == userid and user_input_password == password:
        print("Login Successful!")
        break
    else:
        print("Incorrect User ID or Password. Please try again.")
else:
    print("Too many failed attempts. Program terminated.")