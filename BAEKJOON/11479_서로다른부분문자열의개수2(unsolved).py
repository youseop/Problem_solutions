import sys, math
from itertools import zip_longest, islice
read=sys.stdin.readline

def to_int_keys2(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    cnt = 0
    lastKey = None
    index = {}
    for key in sorted(l):
        if key != lastKey:
            index[key] = cnt
            cnt += 1
        lastKey = key
    return [index[v] for v in l]

def suffix_matrix_smart(to_int_keys, s):
    n = len(s)
    k = 1
    line = to_int_keys(s)
    ans = [line]
    while max(line) < n - 1:
        line = to_int_keys(
            list(zip_longest(line, islice(line, k, None),
                             fillvalue=-1)))
        ans=line
        k <<= 1
    return ans

a=read().strip()
len_a = len(a)

suffix_index = suffix_matrix_smart(to_int_keys2, a)
print(suffix_index)
SA = list(0 for _ in range(len_a))
for i in range(len_a):
    SA[suffix_index[i]] = i
#print(suffix_index)
#print(SA)
answer = len_a*(len_a+1)//2
before = len(a[SA[0]:])
tmp_a= a[SA[0]:]
for i in range(1,len_a):
    tmp_b= a[SA[i]:]
    before_tmp=len(a[SA[i]:])
    for j in range(min(before_tmp,before)):
        if tmp_a[j] == tmp_b[j]:
            answer-=1
        else:
            break
    tmp_a=tmp_b
    before = before_tmp
    #print(answer,'##',a[SA[i-1]:],a[SA[i]:])
print(answer)
