def solution(msg):
    answer = []
    dic = dict()
    for i in range(26):
        dic[chr(i+65)] = i + 1
    last_dic = 26
    print(dic)

    left = 0
    right = 1
    save1 = ''
    save2 = ''
    while left<right and right<=len(msg):
        save2 = msg[left:right]
        if save2 in dic:
            save1 = save2
            if right == len(msg):
                answer.append(dic[save2])
            right += 1
        else:
            last_dic += 1
            dic[save2] = last_dic
            answer.append(dic[save1])
            left = right - 1

    return answer