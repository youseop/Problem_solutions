import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline


def solution(dartResult):
    n = len(dartResult)
    answer = 0
    results = []
    tmp = []
    i = 0
    while i < n:
        if tmp and dartResult[i].isnumeric():
            if tmp[0] == '1' and dartResult[i] == '0':
                tmp[0] = '10'
            else:
                results.append(tmp)
                number = dartResult[i]
                tmp = [number]
        else:
            tmp.append(dartResult[i])
        i+=1

    results.append(tmp)
    double = 0
    for result in results[::-1]:
        a = int(result[0])
        if result[1] == 'D':
            a **=2
        elif result[1] == 'T':
            a **=3

        if double:
            a *= 2
        double = 0
        if len(result)==3:
            if result[2] == '#':
                a *= (-1)
            else:
                a *= 2
                double = 1
                
        answer += a
        
    return answer


print(solution("10S10S#0S"))
