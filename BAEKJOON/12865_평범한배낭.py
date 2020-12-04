import sys
read=sys.stdin.readline

n,k=map(int,read().split())
things=list(list(map(int,read().split())) for _ in range(n))

dp=dict()
dp[0]=0

for w,v in things:
    tmp=[]
    for dp_w, dp_v in dp.items():
        if dp_w + w <= k:
            tmp.append((dp_w + w,dp_v+v))
    for tmp_w, tmp_v in tmp:
        if tmp_w in dp:
            if dp[tmp_w] < tmp_v:
                dp[tmp_w] = tmp_v
        else:
            dp[tmp_w] = tmp_v

print(max(dp.values()))

