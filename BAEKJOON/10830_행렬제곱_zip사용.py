import sys
read=sys.stdin.readline

def mul(a,b):
    b = list(x for x in zip(*b))
    matrix = list(list(0 for _ in range(n)) for _ in range(n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = sum(x*y for x,y in zip(a[i],b[j])) % 1000
    return matrix

n, b = map(int,read().split())
matrix = list(list(map(int,read().split())) for _ in range(n))
answer = list(list(0 for _ in range(n)) for _ in range(n))

for i in range(n):
    answer[i][i] = 1

for i in range(len(bin(b))-1):
    x = 1 << i
    if x > b: break
    if x | b == b:
        answer = mul(answer, matrix)
    matrix = mul(matrix,matrix)

for a in answer:
    print(*a)



