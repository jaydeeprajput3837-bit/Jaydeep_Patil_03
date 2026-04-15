correct_userid = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    userid = input("Enter user ID: ")
    password = input("Enter password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Incorrect user ID or password.")

        if attempts > 0:
            print("Try again. Attempts left:", attempts)
        else:
            print("To many failed attempts. Program terminated.")