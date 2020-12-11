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