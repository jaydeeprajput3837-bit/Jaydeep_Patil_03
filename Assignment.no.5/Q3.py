# Accept number of passenger and ticket cost
n = int(input("Enter number of passenger: "))
ticket_cost = int(input("Enetr cost per ticket: "))

total_amount = 0

for i in range(1, n + 1):
    age = int(input(f'Enter age of passenger {i}: '))

    if age < 12:
        discount = 0.30
        final_cost = ticket_cost - (ticket_cost * discount)
        print(f'Passenger {i}: child(13% discount) -> cost - {final_cost}')

    elif age > 59:
        discount = 0.50
        final_cost = ticket_cost - (ticket_cost * discount)
        print(f'Passenger {i}: senior citizen (50% discount)-> cost = {final_cost}')

    else:
        final_cost = ticket_cost
        print(f'Passenger {i}: No discount -> cost = {final_cost}')

    total_amount += final_cost

print("\nTotal amount to be paid =", total_amount)