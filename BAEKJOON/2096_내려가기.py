import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

n = int(read())
a,b,c = map(int,read().split())
maxa,maxb,maxc = a,b,c
for _ in range(n-1):
    tmpa,tmpb,tmpc = map(int,read().split())
    a,b,c = tmpa + min(a,b),tmpb + min(a,b,c),tmpc + min(c,b)
    maxa,maxb,maxc = tmpa + max(maxa,maxb),tmpb + max(maxa,maxb,maxc),tmpc + max(maxc,maxb)

print(max(maxa,maxb,maxc),min(a,b,c))