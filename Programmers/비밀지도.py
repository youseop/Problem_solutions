def solution(n, arr1, arr2):
    answer = []
    for k in range(n):
        arr = arr1[k] | arr2[k]
        tmp = ""
        for i in range(n):
            if arr | (1<<i) == arr:
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp[::-1])
    return answer