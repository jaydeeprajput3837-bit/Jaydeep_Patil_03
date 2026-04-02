#Convert the time intered
H = int(input("Enter hours: "))
M = int(input("Enter minutes: "))
S = int (input("Enter second: "))

#Calculate the H-M-S
total_seconds = H * 3600 + M * 60 + S

print("Total second =", total_seconds)