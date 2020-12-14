## 책 261p 참고 코드

import sys
sys.stdin = open("TextFile1.txt","rt")
read=sys.stdin.readline

def quick_sort(arr, left, right):
    l,r=left,right
    pivot=arr[(l+r)//2]

    while l <= r:
        while arr[l]<pivot:
            l+=1
        while arr[r]>pivot:
            r-=1
        if l<=r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1

    if left < r: quick_sort(arr, left, r)
    if l<right: quick_sort(arr,l,right)

num = list(int(read()) for _ in range(int(read())))
quick_sort(num,0,len(num)-1)

for n in num:
    print(n)

## 내 코드 but 비효율적
import sys
read=sys.stdin.readline

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left_arr, eq_arr, right_arr = list(), list(), list()
    for n in arr:
        if n < pivot:
            left_arr.append(n)
        elif n == pivot:
            eq_arr.append(n)
        else:
            right_arr.append(n)
    return quick_sort(left_arr) + eq_arr + quick_sort(right_arr)

num = list(int(read()) for _ in range(int(read())))
for n in quick_sort(num):
    print(n)