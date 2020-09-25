import sys
sys.stdin = open('input.txt', 'rt')

'''input'''
n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white, blue = 0, 0

'''dividing function'''


def divide(a, b, n):
    global white, blue
    save = paper[a][b]
    if n == 1:
        if save == 1:
            blue += 1
        else:
            white += 1
        return
    else:
        for i in range(a, a+n):
            for j in range(b, b+n):
                if save != paper[i][j]:
                    divide(a, b, n//2)
                    divide(a, b+n//2, n//2)
                    divide(a+n//2, b, n//2)
                    divide(a+n//2, b+n//2, n//2)
                    return

    if save == 1:
        blue += 1
    else:
        white += 1
    return


'''output'''
divide(0, 0, n)
print(white, blue, sep='\n')
