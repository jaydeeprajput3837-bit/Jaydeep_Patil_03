# Input two numbers
A = int(input("Enter first number: "))
B = int(input("Enter second number "))

# Swap using third variable
Temp = A
A = B
B = Temp

print("After swapping:")
print("A =", A)
print("B =", B)