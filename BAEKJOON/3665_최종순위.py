import sys,gc
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

def getSequence():
    buffer = -1
    answer = []
    for i in range(n):
        if need[i] == 0:
            if buffer != -1:
                return "?"
            buffer = i
    
    for _ in range(n):
        a = buffer
        if a == -1:
            return ["IMPOSSIBLE"]
        answer.append(a)
        buffer = -1
        for i in next[a]:
            need[i] -= 1
            if need[i] == 0:
                if buffer != -1:
                    return ["?"]
                buffer = i

    return list(map(lambda x : x + 1, answer))


for _ in range(int(read())):
    n = int(read())
    num = list(map(lambda x : int(x)-1 ,read().split()))
    m = int(read())
    changed = list(list(map(lambda x : int(x)-1,read().split())) for _ in range(m))
    
    next = list(set() for _ in range(n))
    need = list(0 for _ in range(n))
    for a in range(n):
        next[num[a]] = set(num[i] for i in range(a+1,n))
        need[num[a]] = a

    for a,b in changed:
        if a in next[b]:
            a,b = b,a
        next[a].remove(b)
        next[b].add(a)
        need[a]+=1
        need[b]-=1
    print(*getSequence())

