# Function to check Armstrong number
def is_armstrong(num):
    order = len(str(num))
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    return sum == num

# Accept range from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Armstrong numbers in the given range:")

for i in range(start, end + 1):
    if is_armstrong(i):
        print(i)