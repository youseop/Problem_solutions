def solution(tickets):
    global flag, City
    answer = ["ICN"]
    tickets.sort(key=lambda x: x[1])
    n = len(tickets)
    check = list(True for _ in range(n))
    flag = 1
    City = []

    def dfs(x):
        global flag, City
        if len(answer) == n+1:
            flag = 2
            City = answer[:]
        for i in range(n):
            if tickets[i][0] == x and check[i] and flag == 1:
                answer.append(tickets[i][1])
                check[i] = False
                dfs(tickets[i][1])
                answer.pop()
                check[i] = True
    dfs("ICN")
    return City
