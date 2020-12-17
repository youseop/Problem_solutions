import sys, math
read=sys.stdin.readline

def suffix_array(txt):
    if not txt:
        return []
    txt += chr(0)
    N = len(txt)

    equivalence = {t: i for i, t in enumerate(sorted(set(txt)))}
    cls = [equivalence[t] for t in txt]
    ns = [(2**i)%N for i in range( int( math.ceil( math.log(N,2))))]

    for n in ns:
        result = sorted(zip(cls, cls[n:]+cls[:n], range(N)))
        result0, result1, inds = list(zip(*result))
        for j in range(1, N):
            cls[inds[j]] = cls[inds[j-1]]
            if (result0[j], result1[j]) != (result0[j-1], result1[j-1]):
                cls[inds[j]] += 1
    return list(list(zip(*result))[2][1:])

n=int(read())
a=read().strip()
len_a = len(a)

SA = suffix_array(a)
answer = 0
before = len_a- SA[0]
for i in range(1,len_a):
    cnt=0
    tmp_len = len_a- SA[i]
    for j in range(min(tmp_len,before)):
        if a[SA[i]:][j] == a[SA[i-1]:][j]:
            cnt+=1
        else:
            break
    before = tmp_len
    answer = max(answer, cnt)
print(answer)


