#Convert to days
Days = int(input("Enter number of Days: "))

#Calculate a year
Years = Days // 365
Remaining_days = Days % 365

#Calculate a week and days
Weeks = Remaining_days // 7
Days_left = Remaining_days % 7

print("years:", Years)
print("week:", Weeks)
print("days:", Days_left)