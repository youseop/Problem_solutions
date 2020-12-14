import sys
read=sys.stdin.readline

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2

    a= merge_sort(arr[:mid])
    b= merge_sort(arr[mid:])
    l_a, l_b = len(a), len(b)

    save_arr = []
    cnt_a,cnt_b=0,0

    while cnt_a < l_a and cnt_b < l_b:
        if a[cnt_a]>b[cnt_b]:
            save_arr.append(b[cnt_b])
            cnt_b+=1
        else:
            save_arr.append(a[cnt_a])
            cnt_a+=1

    save_arr += a[cnt_a:]
    save_arr += b[cnt_b:]

    return save_arr
num= list(int(read()) for _ in range(int(read())))
for x in merge_sort(num):
    print(x)

#heaq.merge함수 사용
import sys
read=sys.stdin.readline
from heapq import merge

def merge_sort_heap(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2

    a= merge_sort_heap(arr[:mid])
    b= merge_sort_heap(arr[mid:])
    return list(merge(a,b))
num= list(int(read()) for _ in range(int(read())))
for x in merge_sort_heap(num):
    print(x)