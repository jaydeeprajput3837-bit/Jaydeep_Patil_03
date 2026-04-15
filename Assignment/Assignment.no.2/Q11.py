# Input amount
Amount = int(input("Enter amount: "))

Notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("\nminimum number of notes:")

for note in Notes: 
    count = Amount // note
    if count > 0:
        print(note, ":", count)
        Amount = Amount % note