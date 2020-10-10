def solution(board, moves):
    answer = 0
    a = len(board)
    b = len(board[1])

    save = []

    for m in moves:
        m = m-1
        for i in range(a):
            if board[i][m] != 0:
                save.append(board[i][m])
                board[i][m] = 0
                break
        if len(save) >= 2 and save[-1] == save[-2]:
            save.pop()
            save.pop()
            answer += 2

    return answer
