import sys
numbs = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    numbs.append(n)
maxnum = max(numbs)
check = list(True for _ in range(maxnum+1))
check[0] = False
check[1] = False
x = 2
while x != maxnum:
    if check[x]:
        for i in range(x*2, maxnum, x):
            check[i] = False
    x += 1

for numb in numbs:
    i = 2
    while True:
        if check[i] and check[numb-i]:
            print(numb, '=', i, '+', numb-i)
            break
        i += 1
