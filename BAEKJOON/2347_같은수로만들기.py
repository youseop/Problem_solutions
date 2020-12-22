import sys
sys.stdin = open('text.txt','rt')
read=sys.stdin.readline
from collections import deque

def plus(left, right):
    cnt = 0
    if left == right: return num[left], 0
    tmp = 0
    max_index = [left]
    for i in range(left, right + 1):
        if num[i] > tmp:
            max_index = [i]
            tmp = num[i]
        elif num[i] == tmp:
            max_index.append(i)

    index = left
    for i in max_index:
        if i != index:
            x, c = plus(index, i-1) 
            cnt += (num[max_index[0]] - x)
            cnt += c
        index = i+1

    if index!=n and index <= right:
        x, c = plus(index,right)
        cnt += (num[max_index[0]] - x)
        cnt += c

    return num[max_index[0]], cnt

n = int(read())
num = list(int(read()) for _ in range(n))
print(plus(0,n-1)[1])