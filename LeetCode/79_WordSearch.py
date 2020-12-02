class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        n = len(board)
        m = len(board[0])
        length = len(word)
        check = list(list(True for _ in range(m)) for _ in range(n))
        point = list()
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    point.append((i, j))

        global flag
        flag = False
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        def DFS(a, b, i):
            print(a, b)
            global flag
            if flag:
                return
            if i == length:
                flag = True
                return
            for x, y in zip(dx, dy):
                ax, by = a+x, b+y
                if 0 <= ax < n and 0 <= by < m and check[ax][by]:
                    if word[i] == board[ax][by]:
                        check[ax][by] = False
                        DFS(ax, by, i+1)
                        check[ax][by] = True
        for i, j in point:
            check[i][j] = False
            DFS(i, j, 1)
            check[i][j] = True

        return flag
