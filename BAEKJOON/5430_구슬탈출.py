import sys
read = sys.stdin.readline

for _ in range(int(read())):
    operations = list(read().strip())
    n = int(read())
    if n:
        num = list(read()[1:-2].split(','))
    else:
        tmp = read()
        num = []

    l,r = 0,n-1
    reversed = False
    for operation in operations:
        if operation == 'R':
            reversed = not reversed
        elif operation == 'D':
            if l > r:
                print('error')
                break
            if reversed:
                r -= 1
            else:
                l += 1
    else:
        if reversed:
            result = num[l:r+1][::-1]
        else:
            result = num[l:r+1]
        print('['+','.join(result)+']')
