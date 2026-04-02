# Enter user id and password
correct_userid = "admin"
correct_password = "1234"

# User input 
userid = input("Enter uer ID: ")
password = input("Enter password: ")

# Checking
if userid == correct_userid and password == correct_password:
    print("Login successful ")
else:
    print("Invalid user ID or Password ")