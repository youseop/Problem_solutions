from collections import deque

def solution(s):
    if len(s)%2: return 0
    left = deque(s[:2])
    right = deque(s[2:])
    while right:
        if len(left)>=2 and left[-2] == left[-1]:
            left.pop()
            left.pop()
        left.append(right.popleft())
    if len(left)>=2 and left[-2] == left[-1]:
        left.pop()
        left.pop()
    if left:
        return 0
    else: 
        return 1