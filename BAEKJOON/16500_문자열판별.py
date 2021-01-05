import sys
read=sys.stdin.readline
sys.setrecursionlimit(100000)
mask = list(read().strip())
n = int(read())
strings = list(read().strip() for _ in range(n))

dp = list(-1 for _ in range(len(mask)))

def dfs(index):
    if index == len(mask):
        return 1
    if dp[index]>=0:
        return dp[index]
    save = 0
    for string in strings:
        if len(mask) - index >= len(string) and list(string) == mask[index:index+len(string)]:
            save += dfs(index + len(string))
    dp[index] = save
    return save

dfs(0)
if dp[0]:
    print(1)
else:print(0)