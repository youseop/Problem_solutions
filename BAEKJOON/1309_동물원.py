import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

n = int(read())
a,b = 1,3

for i in range(2,n+1):
    b,a = a+2*b,b


print(b%9901)