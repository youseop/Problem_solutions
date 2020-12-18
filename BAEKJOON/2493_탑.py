import sys
read=sys.stdin.readline

n=int(read())
tower = list(map(int,read().split()))
stack = []
get_signal = list(0 for _ in range(n))

for i in range(n-1,-1,-1):
    while stack and tower[stack[-1]] < tower[i]:
        get_signal[stack.pop()] = i+1
    stack.append(i)

print(*get_signal)
        

