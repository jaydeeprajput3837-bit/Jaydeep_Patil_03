n = 5

for i in range(1, n + 1):
    for s in range(n - i):
        print("", end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    if i != n:
        for s in range(2 * (n - i)):
            print("  ", end="")

    for j in range(i, 0, -1):
        if i == n and j == i:
            continue
        print(j, end=" ")

    print()