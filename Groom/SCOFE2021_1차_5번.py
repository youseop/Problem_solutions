# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
read = sys.stdin.readline


def dfs(i):
	cnt = 0
	point = deque([(0,i)])
	screen = list(s[::] for s in screen_sample)
	screen[0][i] = 0
	
	while point:
		a,b = point.popleft()
		for x,y in [(0,1),(0,-1),(1,0)]:
			ax,by = a+x,b+y
			if 0<=ax<n and 0<=by<m and screen[ax][by]=='.':
				if x:
					screen[ax][by] = screen[a][b]
				else:
					screen[ax][by] = screen[a][b] + 1
				point.append((ax,by))
				
	cnt = sys.maxsize
	for i in range(m):
		if type(screen[n-1][i]) == type(0):
			cnt = min(cnt, screen[n-1][i])
			
	return cnt
		

m,n = map(int,read().split())
screen_sample = list(list(read().strip()) for _ in range(n))

res = sys.maxsize
for i in range(m):
	if screen_sample[0][i] == 'c':
		res = min(res, dfs(i))
		
if res == sys.maxsize:
	print(-1)
else:
	print(res)
