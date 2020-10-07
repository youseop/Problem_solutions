import sys

n, m = map(int, input().split())
alph = list(sys.stdin.readline().split())
alph.sort()

aeiou = set(['a', 'e', 'i', 'o', 'u'])
save = []
check = []
answer = []

if n < 3:
    sys.exit()


def dfs():
    if len(save) == n:
        set_save = set(save)
        tmpa = aeiou & set_save
        tmpb = set_save-aeiou
        tmpa = list(tmpa)
        tmpb = list(tmpb)
        _save = save[:]
        if len(tmpa) > 0 and len(tmpb) > 1:
            _save.sort()
            tmp = ""
            for i in _save:
                tmp += i
            answer.append(tmp)
        return
    for i in range(check[-1]+1, m):
        check.append(i)
        save.append(alph[i])
        dfs()
        check.pop()
        save.pop()


for i in range(m):
    check.append(i)
    save.append(alph[i])
    dfs()
    check.pop()
    save.pop()

for x in answer:
    print(x)
