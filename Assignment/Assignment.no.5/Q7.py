n= int(input("Enter n: "))
fact = 1
sum = 0

for i in range(1, n + 1):
    fact *= i
    sum += fact

print("Sum of factorial series:", sum)


N = int(input("Enter a value of N: "))
sum = 0

for i in range(1, N + 1):
    sum += N ** i

print("Sum of power series:", sum)



n = int(input("Enter number of terms: "))
sum = 0
term = 1

for i in range(n):
    sum += term
    term *= 2

print("Sum of geometric series:", sum)



a = int(input("Enter value of a: "))
syum = 0

for i in range(1, 11):
    sum += (a ** i) / i

print("Sum of series:", sum)



x = int(input("Enter va;ue of x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1
den = 1

for i in range(1, n + 1):
    sum += sign * (x ** i) / den
    sign *= -1
    den += 2

print("Sum of series:", sum)