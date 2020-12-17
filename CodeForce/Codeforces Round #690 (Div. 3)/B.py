import sys, math
read=sys.stdin.readline
from collections import deque

N = int(read())

for _ in range(N):
    n = int(read())
    tmp=read().strip()
    num=[]
    for i in tmp:
        num.append(int(i))
    if len(num)<4:
        print('NO')
    else:
        if num[:4] == [2,0,2,0]:
            print('YES')
        elif num[:3] == [2,0,2] and num[-1] == 0:
            print('YES')
        elif num[:2] == [2,0] and num[-2:] == [2,0]:
            print('YES')
        elif num[0] == 2 and num[-3:] == [0,2,0]:
            print('YES')
        elif num[-4:] == [2,0,2,0]:
            print('YES')
        else:
            print('NO')
