# ENter user id and password
import random
correct_userid = "admin"
correct_password = "1234"

# User input
userid = input("Enter user ID: ")
password = input("Enter password: ")

# Verify login
if userid == correct_userid and password == correct_password:
    print("login successful ")

    # Generate 4-digit random number
    captcha = random.randint (1000, 9999)
    print("Enter this number:", captcha)

    user_captcha = int(input("Re-enter the number: "))

    # Verify captcha 
    if user_captcha == captcha:
        print("Verification successful ")
    else:
        print("Verification failed ")

else:
    print("Invalid user ID or Password")