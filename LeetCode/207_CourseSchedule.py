class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque as dq
        course = list(0 for _ in range(numCourses))
        need = dict()
        for i in range(numCourses):
            need[i] = []
        for a, b in prerequisites:
            course[a] += 1
            need[b].append(a)
        cnt = 0
        point = dq([])
        for i in range(numCourses):
            if course[i] == 0:
                point.append(i)
                cnt += 1
        while point:
            a = point.popleft()
            for i in need[a]:
                course[i] -= 1
                if course[i] == 0:
                    point.append(i)
                    cnt += 1

        if cnt == numCourses:
            return True

        else:
            return False
