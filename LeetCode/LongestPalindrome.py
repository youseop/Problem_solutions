class Solution:
    def longestPalindrome(self, s: str) -> int:
        # s=s.upper()
        save = dict()
        for i in s:
            if i in save:
                if save[i][0]:
                    save[i][0] = False
                else:
                    save[i][0] = True
                    save[i][1] += 2
            else:
                save[i] = [False, 0]

        answer = 0
        flag = 1
        for i in save:
            if save[i][0] == False:
                flag = 2
            answer += save[i][1]
        if flag == 2:
            answer += 1
        return answer
