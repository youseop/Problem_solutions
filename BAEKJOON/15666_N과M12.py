import sys
read=sys.stdin.readline

n,m=map(int,read().split())
num = list(map(int,read().split()))
num.sort()

def comb(x,cnt,save):
    if cnt == m:
        print(save)
        return
    before = -1
    for i in range(x,n):
        if num[i] == before:
            continue
        comb(i,cnt+1,save+str(num[i])+" ")
        before = num[i]

comb(0,0,"")    
###############################################
import sys
read=sys.stdin.readline

n,m = map(int,read().split())
NUM=list(map(int,read().split()))
NUM=list(set(NUM))
NUM.sort()
n=len(NUM)

check = set()

def permu(x, cnt , save):
    if cnt == m:
        save_t = tuple(save)
        if save_t not in check:
            check.add(save_t)
            print(save)
        return
    for i in range(x, n):
        permu(i,cnt+1,save+str(NUM[i])+" ")
permu(0,0,"")