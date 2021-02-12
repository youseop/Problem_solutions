
def makeSet(save,str_input):
    dic = {}
    for i in range(len(str_input)-1):
        tmp = str_input[i:i+2]
        if not tmp.isalpha():
            continue

        if tmp not in dic:
            dic[tmp] = 0
        else:
            dic[tmp] += 1
        save.add(tmp+str(dic[tmp]))


def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()

    save1 = set()
    save2 = set()     
    makeSet(save1, str1)
    makeSet(save2, str2)

    union = len(save1 | save2) 
    intersection = len(save1 & save2) 

    if not union and not intersection:
        return 65536
    return int(intersection/union * 65536)