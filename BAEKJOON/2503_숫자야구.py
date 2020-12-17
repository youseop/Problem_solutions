import sys, math
read=sys.stdin.readline

#스트라이크 Count
def strike(a, b):
    a,b = str(a), str(b)
    cnt = 0
    for i in range(3):
        if a[i] == b[i]:
            cnt += 1
    return cnt
#볼 Count
def ball(a, b):
    return len( set(str(a)) & set(str(b)) ) - strike_cnt

#0이 포함되지 않은, 각 자리수가 모두 다른 숫자들에 한해서 탐색! - 문제를 정확하게 읽도록 하자
answer = set(i for i in range(123,988) if '0' not in str(i) and len(set(str(i)))==3)

for _ in range(int(read())):
    num,s,b = map(int,read().split())
    for i in list(answer):
        strike_cnt = strike(i,num)
        if strike_cnt != s or ball(i,num) != b:
            answer -= set([i])

print(len(answer))
