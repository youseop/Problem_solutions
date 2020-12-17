import sys, math
from itertools import zip_longest, islice
sys.stdin = open("TextFile1.txt","rt")
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

SA = list(0 for _ in range(len_a))
for i in range(len_a):
    SA[suffix_index[i]] = i
#print(suffix_index)
for i in range(len_a):
    print(SA[i]+1,end=' ')
print()
print('x',end=' ')

#print(answer,'before')
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
    print(cnt,end=' ')
    #print(answer,'##',a[SA[i-1]:],a[SA[i]:])
