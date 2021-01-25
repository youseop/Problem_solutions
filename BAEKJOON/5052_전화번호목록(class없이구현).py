import sys
read=sys.stdin.readline

def insert(string):
    tmp = T
    for char in string:
        if char not in tmp:
            tmp[char] = {}
        tmp = tmp[char]
        #다음 노드에 'end'가 존재한다면 같은 접두사를 가진 번호가 있다는 의미이다.
        #같은 접두사가 존재한다는 의미로 1을 return
        if 'end' in tmp:
            return 1
    
    #문자열이 끝나면 다음 노드에 'end'라는 flag입력
    #'end'의 존재 유무로 어느 지점에서 문자열이 종료되었는지 확인!
    tmp['end'] = 1


for _ in range(int(read())):
    T = {}
    nums = list(list(read().strip()) for _ in range(int(read())))
    nums.sort(key = lambda x: len(x))
    for num in nums:
        if insert(num):
            print('NO')
            break
    else:
        print('YES')