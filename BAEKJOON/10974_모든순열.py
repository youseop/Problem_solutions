# n=int(input())
# numbs=list(range(1,n+1))

# import itertools

# answer=list(itertools.permutations(numbs))
# for x in answer:
#     print(*x)

# itertools 사용!


n = int(input())
numbs = list(range(1, n+1))

save = []


def function():
    if len(save) == n:
        print(*save)

    for i in range(1, n+1):
        if i not in save:
            save.append(i)
            function()
            save.pop()


function()
