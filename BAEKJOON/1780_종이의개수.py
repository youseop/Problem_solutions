import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

z, mo, po = 0, 0, 0


def divthree(a, b, n):
    global z, mo, po
    save = paper[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if paper[i][j] != save:
                dx = [0, n//3, n//3*2]
                dy = [0, n//3, n//3*2]
                for x in dx:
                    for y in dy:
                        divthree(a+x, b+y, n//3)
                return
    if save == 0:
        z += 1
    elif save == -1:
        mo += 1
    else:
        po += 1
    return


divthree(0, 0, n)
print(mo, z, po, sep='\n')
