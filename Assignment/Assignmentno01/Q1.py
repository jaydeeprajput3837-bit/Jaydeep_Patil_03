#Input marks of 5 subject
sub1 = int(input("Ent marks of sub1: "))
sub2 = int(input("Ent marks of sub2: "))
sub3 = int(input("Ent marks of sub3: "))
sub4 = int(input("Ent marks of sub4: "))
sub5 = int(input("Ent marks of sub5: "))

#Calculate total sub
Total = sub1 + sub2 + sub3 + sub4 + sub5

#Calculate percentage
percentage = (Total / 500 ) * 100

#Display result
print("total marks = ", Total)
print("percentage =", percentage)