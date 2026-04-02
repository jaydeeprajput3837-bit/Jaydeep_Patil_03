# Total amount of tickets
total_amount = 0

for i in range(1, 6):
    print(f"\nPerson {i}")
    
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))
    
    # Apply discount
    if age < 12:
        final_amount = ticket - (ticket * 0.30)
    elif age > 59:
        final_amount = ticket - (ticket * 0.50)
    else:
        final_amount = ticket
    
    print("Amount to pay:", final_amount)
    
    total_amount += final_amount

print("\nTotal amount for all persons =", total_amount)