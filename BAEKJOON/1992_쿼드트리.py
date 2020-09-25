import sys
sys.stdin = open('input.txt', 'rt')

'''input'''
n = int(input())
vid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
answer = ''

'''dividing function'''


def div(a, b, n):
    global answer
    save = vid[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if vid[i][j] != save:
                answer += '('
                div(a, b, n//2)
                div(a, b+n//2, n//2)
                div(a+n//2, b, n//2)
                div(a+n//2, b+n//2, n//2)
                answer += ')'
                return
    if save == 0:
        answer += '0'
    else:
        answer += '1'


'''output'''
div(0, 0, n)
print(answer)
