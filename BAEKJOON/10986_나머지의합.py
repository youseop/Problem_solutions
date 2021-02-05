import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

n,m = map(int,read().split())
num = [0]+list(map(int,read().split()))
mod = {0: 1}

for i in range(1,n+1):
    num[i] = (num[i-1]+num[i])%m
    if num[i] not in mod:
        mod[num[i]] = 1
    else:
        mod[num[i]] += 1
answer = 0
for i in mod.keys():
    x = mod[i]
    answer += x*(x-1)//2

print(answer)
#https://www.acmicpc.net/source/5751779