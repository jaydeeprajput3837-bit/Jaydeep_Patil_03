n = 5

for i in range(n):
    print('  ' * (n - i - 1), end=' ')
    ch = ord('A')
    for j in range(2*i + 1):
        print(chr(ch), end=' ')
        ch += 1
    print()