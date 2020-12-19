import sys
sys.stdin = open('text.txt','rt')
read=sys.stdin.readline

def largest():
    answer = 0
    for i in range(n):
        if i != 0 and rect[i] == rect[i-1]:
            continue

        l,r = i,i
        while True:
            flag = 0
            if l-1 >= 0 and rect[i]<=rect[l-1]:
                l -= 1
            else: flag += 1
            if r+1 < n and rect[i]<=rect[r+1]:
                r += 1
            else: flag += 1

            if flag == 2: break
        answer = max(answer, rect[i]*(r-l+1))
        #print(rect[i]*(r-l+1))
        
    return answer

while 1:
    n,*rect = list(map(int,read().split()))
    if n == 0: break
    print(largest())