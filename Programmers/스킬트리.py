def solution(skill, skill_trees):
    answer = 0
    alph = list(-1 for _ in range(91))

    for index, x in enumerate(skill):
        alph[ord(x)] = index+1

    for sentence in skill_trees:
        flag = 1
        save = 0
        for a_chr in sentence:
            a_int = ord(a_chr)
            if alph[a_int] != -1:
                if save+1 == alph[a_int]:
                    save = alph[a_int]
                else:
                    flag = 2
        if flag == 1:
            answer += 1

    return answer
