import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

#n,v = map(int,read().split())
#things = list(list(map(int,read().split())) for _ in range(n))
#dp = list(0 for _ in range(v+1))

#for weight,value in things:
#    for i in range(v-weight,-1,-1):
#        dp[i+weight] = max(dp[i+weight],dp[i]+value)

#print(dp[-1])

n,v = map(int,read().split())
things = list(list(map(int,read().split())) for _ in range(n))

dp = dict()
dp[0] = 0

for weight,value in things:
    _dp = []
    for dp_w,dp_v in dp.items():
        if dp_w + weight <= v:
            _dp.append((dp_w+weight,dp_v+value))
    for new_w,new_v in _dp:
        if new_w in dp:
            if dp[new_w] < new_v:
                dp[new_w] = new_v
        else:
            dp[new_w] = new_v
print(max(dp.values()))