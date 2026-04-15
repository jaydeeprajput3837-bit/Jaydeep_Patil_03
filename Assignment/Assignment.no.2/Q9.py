# Input two numbers
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))

# Swapping without third variable
A, B = B, A

print("After swapping:")
print("A =", A)
print("B =", B)