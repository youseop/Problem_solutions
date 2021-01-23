def solution(gems):
    import sys
    n=len(gems)
    answer = []
    tot_gems = set(gems)
    tot_n = len(tot_gems)
    
    shopping = dict()
    save_len = sys.maxsize
    save_point = []
    start,end = 0,0

    while start <= end:
        if len(shopping) < tot_n:
            if end == n:
                break
            if gems[end] in shopping:
                shopping[gems[end]] += 1
            else:
                shopping[gems[end]] = 1

            end +=1
        elif len(shopping) == tot_n:
            if save_len > end-start:
                save_point = [start+1,end]
                save_len = end - start

            shopping[gems[start]] -= 1
            if shopping[gems[start]] == 0:
                shopping.pop(gems[start])

            start += 1
        else:
            shopping[gems[start]] -= 1
            if shopping[gems[start]] == 0:
                shopping.pop(gems[start])

            start += 1

    answer = save_point
    return answer