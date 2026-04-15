# Input marks of 5 subject
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

# Calculate total marks and percentage
Total = m1 + m2 + m3 + m4 + m5
Percentage = Total / 5

print("Total =", Total)
print("Percentage =", Percentage)

# Decide grade
if Percentage >= 60:
    print("Grade: First class")
elif Percentage >= 50:
    print("Grade: Second class")
elif Percentage >= 40:
    print("Grade: Pass class")
else:
     print("Grade: Fail")