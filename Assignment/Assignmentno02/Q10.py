# Input three-digit number
Num = int(input("Enter a three-digit number: "))

# Extract digits
A = Num // 100
B = (Num // 10) % 10
C = Num % 10

# Reverse number
Reverse = (C * 100) + (B * 10) + A

print("Reverse number =", Reverse)