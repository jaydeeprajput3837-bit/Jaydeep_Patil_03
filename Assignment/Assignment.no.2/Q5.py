#Calculate selling price 
CP = int(input("Enter cost price of book: "))
Discount_percent = int(input("Enter discount percentage: "))

Discount = (CP * Discount_percent) / 100
SP = CP - Discount

print("Discount amount =", Discount)
print("Selling price=", SP)