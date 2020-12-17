import sys, math
from itertools import zip_longest, islice
from collections import defaultdict
sys.stdin = open("TextFile1.txt","rt")
read=sys.stdin.readline

def sort_bucket(s, bucket, order):
    d = defaultdict(list) 
    for i in bucket: 
        key = s[i:i+order] 
        d[key].append(i) 
    result = [] 
    for k,v in sorted(d.items()): 
        if len(v) > 1: 
            result += sort_bucket(s, v, order*2) 
        else: 
            result.append(v[0]) 
    return result 

a=read().strip()
len_a = len(a)

SA = sort_bucket(a, (i for i in range(len(a))), 1)
#print(SA)
#SA = list(0 for _ in range(len_a))
#for i in range(len_a):
#    SA[suffix_index[i]] = i
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
