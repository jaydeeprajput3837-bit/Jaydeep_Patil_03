# Check a side of triangle is equilatetral, isosceles,scalene
A = int(input("Enter first side: "))
B = int(input("Enter second side: "))
C = int(input("Enter third side: "))

# First check if triangle is valid
if A + B > C and A + C > B and B + C > A:

    if A == B and B == C:
        print("Equilatearal Triangle")
    elif A == B or B == C or A == C:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Triangle is not Valid")