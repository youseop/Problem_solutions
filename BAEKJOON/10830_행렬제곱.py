import sys
sys.stdin = open('input.txt','rt')

n,m=map(int,sys.stdin.readline().split())
list1=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

save=dict()
tmp=list([0 for _ in range(n)] for _ in range(n))
for i in range(n):
    for j in range(n):
        tmp[i][j]= list1[i][j]%1000
save[1]=tmp


def fun(n,m):
    if m in save:
        return save[m]
    else:
        lista=fun(n,m//2)
        listb=fun(n,m-m//2)
        tmp=list([0 for _ in range(n)] for _ in range(n))

        for i in range(n):
            for j in range(n):
                tmp[i][j]=0
                for x in range(n):
                    tmp[i][j]+=lista[i][x]*listb[x][j]
                tmp[i][j]%=1000
        
        save[m]=tmp
        return save[m]
for x in fun(n,m):
    for i in x:
        print(i,end=' ')
    print()