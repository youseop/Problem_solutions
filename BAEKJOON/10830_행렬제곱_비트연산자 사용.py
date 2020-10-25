import sys
read = sys.stdin.readline

n, b = map(int, read().split())

matrix = list(list(map(int, read().split())) for _ in range(n))
# 행렬 곱셈 함수


def mul(a, b):
    new = list(list(0 for _ in range(n)) for _ in range(n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new[i][j] += a[i][k]*b[k][j]
            new[i][j] %= 1000
    return new


# I 행렬을 기본값으로 세팅
answer = list(list(0 for _ in range(n)) for _ in range(n))
for i in range(n):
    answer[i][i] = 1
# 포문을 한번 돌 때마다 matrix는 제곱이 되고,
# 이진수로 바꿨을 때, 1이 있는 지점마다 matrix를 answer에 곱해준다.
for i in range(len(bin(b))-1):
    tmp = 1 << i
    if tmp & b:
        answer = mul(answer, matrix)

    matrix = mul(matrix, matrix)

for a in answer:
    print(*a)
