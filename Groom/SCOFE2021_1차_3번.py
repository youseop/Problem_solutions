# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
read = sys.stdin.readline


def check(size,x,y):
	if x < n and y < n:
		for i in range(size):
			for j in range(size):
				if space[x+i][y+j] == 0:
					return False
		return True
	else:
		return False

def cntBlock(size):
	cnt = 0
	for i in range(n-(size-1)):
		for j in range(n-(size-1)):
			if space[i][j] and check(size,i,j):
				cnt += 1

	return cnt

n = int(read())
space = list(list(map(int,read().strip())) for _ in range(n))
res = []
for i in range(1,n+1):
	t = cntBlock(i)
	if t == 0: 
		break
	res.append(t)
	
print('total:',sum(res))
for i,x in enumerate(res):
	print('size[',i+1,']: ',x,sep='')

