import sys
read=sys.stdin.readline

def mul(a,b):
    matrix = list(list(0 for _ in range(n)) for _ in range(n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = sum(list(x*y for x,y in zip(
                a[i],
                list(b[x][j] for x in range(n))
                )))%1000
    return matrix

n, b = map(int,read().split())
matrix = list(list(map(int,read().split())) for _ in range(n))

#정답을 저장할 행렬 I 생성 - answer
answer = list(list(0 for _ in range(n)) for _ in range(n))
for i in range(n):
    for j in range(n):
        if i == j:
            answer[i][j] = 1

i=0
while (1<<i) < b:
    if (1<<i) | b == b:
        answer = mul(answer,matrix)
    matrix = mul(matrix,matrix)
    i+=1

for a in answer:
    print(*a)

