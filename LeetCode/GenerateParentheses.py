class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def bracket(left, right, x, case):
            if x == n*2:
                answer.append(case)
                return
            if left < n:
                bracket(left+1, right, x+1, case+"(")
            if right < left:
                bracket(left, right+1, x+1, case+")")

        bracket(0, 0, 0, "")
        return answer
