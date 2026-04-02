# Input cost price and selling price
CP = int(input("Enter cost Price: "))
SP = int(input("Enter selling Price"))

# Calculate profit or loss
if SP > CP:
    profit = SP - CP
    print("Profit =", profit)
elif CP > SP:
    loss = CP - SP
    print("Loss =", loss)
else:
    print("No profit No loss")