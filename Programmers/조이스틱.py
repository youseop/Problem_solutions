def changeAlphabet(x):
    return min(ord(x)-65,91-ord(x))

def chooseAlphabet(string,index):
    n = len(string)
    if string[index]!='A':
        return [index,0]
    for i in range(1,1+n//2):
        mi,pi = index-i,index+i

        if index-i<0:  mi += n
        if index+i>=n: pi -= n

        if string[pi] != 'A':
            return [pi, i]
        elif string[mi] != 'A':
            return [mi, i]
    return [-1,-1]


def solution(string):
    i = 0
    answer = 0
    string = list(string)
    while 1:
        index, diff = chooseAlphabet(string, i)
        if index == -1:
            break
        answer += diff
        answer += changeAlphabet(string[index])
        string[index] = 'A'
        i = index

    return answer