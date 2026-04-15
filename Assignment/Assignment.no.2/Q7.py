# Input three digit number
Num = int(input("Enter a three-digit number: "))

# Extract digit
A = Num // 100        # Hundreds place
B = (Num // 10) % 10  # Tens Place
C = Num % 10          # Ones place

# Calculate sum
sum_digit = A + B + C
print("sum of digit =", sum_digit)