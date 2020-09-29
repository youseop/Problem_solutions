import sys
sys.stdin = open('input.txt', 'rt')
n = 0
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        command[1] = int(command[1])

    if command[0] == 'add':
        if not (n & 1 << command[1]):
            n += 1 << command[1]

    if command[0] == 'remove':
        n = n & ~(1 << command[1])

    if command[0] == 'check':
        if n & 1 << command[1]:
            print(1)
        else:
            print(0)

    if command[0] == 'toggle':
        n ^= 1 << command[1]

    if command[0] == 'all':
        n = (1 << 21)-1

    if command[0] == 'empty':
        n = 0
