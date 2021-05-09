def solution(n, k, cmd):
    check = list('O' for _ in range(n))
    deleted = []

    index = k
    for c in cmd:
        if c[0] == 'D':
            cnt = int(c[2])
            while index < n and cnt > 0:
                index += 1
                if check[index] == 'O':
                    cnt -= 1
        elif c[0] == 'U':
            cnt = int(c[2])
            while index >= 0 and cnt > 0:
                index -= 1
                if check[index] == 'O':
                    cnt -= 1
        elif c[0] == 'C': # 행삭제 후 아래행 선택(맨 아래면 윗행 선택)
            check[index] = 'X'
            deleted.append((index))
            i = index
            while i < n:
                if check[i] == 'O':
                    index = i
                    break
                i += 1
            if i == n:
                i = index
                while i >= 0:
                    if check[i] == 'O':
                        index = i
                        break
                    i -= 1
        else: #삭제된 행을 복구
            i = deleted.pop()
            check[i] = 'O'

    return ''.join(check)