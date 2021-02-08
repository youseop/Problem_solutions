import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

def toNum(x):
    return ord(x) - 65

def toChr(x):
    return chr(x + 65)

def dfs1(x):
    if x == -19:
        return
    print(toChr(x),end='')
    for i in bridge[x]:
        dfs1(i)
    return

def dfs2(x):
    if x == -19:
        return
    dfs2(bridge[x][0])
    print(toChr(x),end='')
    dfs2(bridge[x][1])

def dfs3(x):
    if x == -19:
        return
    for i in bridge[x]:
        dfs3(i)
    print(toChr(x),end='')
    return


n = int(read())
bridge = list([] for _ in range(n))

for _ in range(n):
    me, left, right = read().split()
    bridge[toNum(me)].append(toNum(left))
    bridge[toNum(me)].append(toNum(right))
    
dfs1(0)
print()
dfs2(0)
print()
dfs3(0)
print()
