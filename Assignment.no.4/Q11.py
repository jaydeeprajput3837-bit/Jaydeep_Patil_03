n = int(input("Enter a number: "))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10

   # Find factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum += fact 
    temp //= 10

if sum == n:
    print("Strong number")
else:
    print("Not a strong number")