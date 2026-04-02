#Branching number digit
num = int(input('Enter 3 digit number:'))
temp = num

#Calculate the value
d1 = temp % 10
temp = temp // 10
 
d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp //= 10

rev = d1 * 100 + d2 * 10 + d3
if(num == rev):
    print(f'{num} is a pallindrome number.')
else:
    print(f'{num} is not a pallindrome number.')