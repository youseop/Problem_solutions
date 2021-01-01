import sys
read=sys.stdin.readline

n = int(read())
a = 1
b = 2
if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()
for i in range(n-2):
    a,b = b,(a+b)%15746
    
print(b)