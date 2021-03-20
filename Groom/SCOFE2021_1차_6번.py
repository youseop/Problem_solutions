# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
read = sys.stdin.readline

m,n = map(int,read().split())
store = list(list(map(int,read().split())) for _ in range(n))

for i in range(1,n):
	store[i][0] += store[i-1][0]
	
for i in range(1,m):
	store[0][i] += store[0][i-1]

for i in range(1,n):
	for j in range(1,m):
		store[i][j] += max(store[i-1][j],store[i][j-1])

print(store[-1][-1])
