import sys
read=sys.stdin.readline

bracket = read().strip()
stack = []

for i in bracket:
    if i =='(' or i =='[': stack.append(i)
    elif i == ']':
        sum = 0
        while stack:
            tmp = stack.pop()
            if type(tmp) == type(1):
                sum+=tmp
            elif tmp == '[':
                if sum==0: stack.append(3)
                else: stack.append(sum*3)
                break
            else: 
                print(0)
                exit()
    else:
        sum = 0
        while stack:
            tmp = stack.pop()
            if type(tmp) == type(1):
                sum+=tmp
            elif tmp == '(':
                if sum==0: stack.append(2)
                else: stack.append(sum*2)
                break
            else: 
                print(0)
                exit()

br=['(',')','[',']']
if any(i in stack for i in br):
    print(0)

else:
    sum=0
    for i in stack:
        sum+=i
    print(sum)
   