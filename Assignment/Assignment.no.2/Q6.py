#Input basic salary
Basic = int(input("Enter basic salary: "))

# Calculate allowances
DA = 0.10 * Basic
TA = 0.12 * Basic
HRA = 0.15 * Basic

# Calculate total salary
Total_Salary = Basic + DA + TA + HRA

# Display results
print("Basic salary:", Basic)
print("DA (10%):", DA)
print("TA (12%):", TA)
print("HRA (15%):", HRA)
print("Total Salary:", Total_Salary)
