# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
read = sys.stdin.readline


def parseTime(s):
	h,m = s.strip().split(':')
	return int(h)*60 + int(m)


def makeReadable(x):
	h = x // 60
	m = x % 60
	if m < 10:
		m = '0'+str(m)
	else:
		m = str(m)
	if h < 10:
		h = '0'+str(h)
	else:
		h = str(h)
	return h+':'+m


n = int(read())
times = list(list(read().strip().split('~')) for _ in range(n))

start,end = 0,sys.maxsize
for time in times:
	s,e = parseTime(time[0]),parseTime(time[1])
	start,end = max(start,s), min(end,e)
if (start <= end):
	print(makeReadable(start),'~',makeReadable(end))
else:
	print(-1)