import sys, math
read=sys.stdin.readline

a=read().strip()
b=read().strip()

#문자열들을 구분해주기 위해 가운데에 $ 삽입
new = a+"$"+b
len_new,len_a = len(new),len(a)

#(접미사 문자열, 문자열의 길이, 문자열 a 포함여부)
suffix = list((new[i:], len_new-i, True) if i < len_a else (new[i:], len_new-i, False) for i in range(len_new))
#접미사 문자열이 사전순으로 위치하도록 정렬
suffix.sort()

lcs_len = 0
lcs=""
for i in range(1,len_new):
    cnt = 0
    pointer=0
    if suffix[i][2] != suffix[i-1][2]:
        #두 문자열 중 길이가 짧은 문자열을 기준으로 탐색(ERROR: out of range 방지)
        for j in range(min(suffix[i][1],suffix[i-1][1])):
            #단어를 앞에서부터 하나하나 비교해 나간다. 
            if suffix[i][0][j] == suffix[i-1][0][j]:
                cnt+=1
                pointer = j
            else:
                break
        lcs_len=max(cnt,lcs_len)
        if cnt == lcs_len:
            lcs = suffix[i][0][:pointer+1]
#길이와 공통 부분 문자열을 출력한다.(확인을 위해 추가로 출력해 주었다.)
print(lcs_len, lcs)
