from collections import deque
import sys
read = sys.stdin.readline


def BFS(a, b):
    point = deque([a])
    dslr = list(-1 for _ in range(10_000))
    dslr[a] = [-1, -1]

    while point:
        x = point.popleft()
        if x == b:
            answer = deque([])
            while True:
                i, j = dslr[x]
                if i == -1:
                    break
                answer.appendleft(j)
                x = i
            print(''.join(answer))

        if dslr[2*x % 10_000] == -1 and dslr[2*x % 10_000] == -1:
            point.append(2*x % 10_000)
            dslr[2*x % 10_000] = [x, 'D']

        if x < 1 and dslr[9999] == -1:
            point.append(9999)
            dslr[9999] = [x, 'S']
        elif x >= 1 and dslr[x-1] == -1:
            point.append(x-1)
            dslr[x-1] = [x, 'S']

        tmp1 = x//1000
        tmp2 = (x % 1000)//100
        tmp3 = (x % 100)//10
        tmp4 = (x % 10)
        l_tmp = 1000*tmp2+100*tmp3+10*tmp4+tmp1
        r_tmp = 1000*tmp4+100*tmp1+10*tmp2+tmp3

        if dslr[l_tmp] == -1:
            point.append(l_tmp)
            dslr[l_tmp] = [x, 'L']
        if dslr[r_tmp] == -1:
            point.append(r_tmp)
            dslr[r_tmp] = [x, 'R']


for _ in range(int(read())):
    a, b = map(int, read().split())
    BFS(a, b)
