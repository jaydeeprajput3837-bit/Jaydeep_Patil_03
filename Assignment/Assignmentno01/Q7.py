#Find a roots are quadratic equation
A = int(input("Enter value of (A): "))
B = int(input("Enter value of (B): "))
C = int(input("Enter value of (C): "))

D = B * B - 4 * A * C
if D > 0:
    x1 = (-3 + 1) / (2 * 1)
    x2 = (-3 - 1) / (2 * 1)
    print("Roots are real and different")
    print("x1 =", x1)
    print("x2 =", x2)

elif D == 0:
         x = -B / (2 * A)
         print("x =", x)
    
else:
     print("Roots are complex (not real)")