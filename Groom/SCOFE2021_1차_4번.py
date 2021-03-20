# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
read = sys.stdin.readline


def genereToFavor(a):
	return favor[ord(a)-65]


favor = list(map(float,read().split()))
n,m = map(int,read().split())
wyo = list(list(read().strip()) for _ in range(n))
genre = list(list(read().strip()) for _ in range(n))

contents = []

for i in range(n):
	for j in range(m):
		if wyo[i][j] == 'W': continue
		elif wyo[i][j] == 'Y':
			contents.append((0,genre[i][j],genereToFavor(genre[i][j]),i,j))
		else:
			contents.append((1,genre[i][j],genereToFavor(genre[i][j]),i,j))

contents.sort(key = lambda x : (x[0], -x[2]))		
for content in contents:
	print(*content[1:])

