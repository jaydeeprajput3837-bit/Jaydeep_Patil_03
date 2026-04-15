# check a triangle valid or not
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

# Calculate the angel
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Triangle is Valid")
else:
    print("Triangle is Not Valid")