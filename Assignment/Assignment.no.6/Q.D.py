for i in  range(5):
    ch = ord('A')
    for j in range(i + 1):
        print(chr(ch), end = '  ')
        ch += 1
    print()