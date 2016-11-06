start = int(input("How many lines?"))

for e in range(start, 0, -1):
    for d in range(start - e):
            print(' ', end='')
    for d in range(e):
            print('*', end='')
    print()
