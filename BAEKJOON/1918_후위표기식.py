from collections import deque
import sys
read = sys.stdin.readline

infix = list(read().strip())


ABC = list()  # 알파벳 저장
OP = list()  # 알파벳 외의 수식 저장

for i in infix:

  # 각 수식들의 우선순위가 다르기 때문에 나누어 생각해줘야 한다.
    if i == '+' or i == '-':
      # OP가 비거나 ( 가 등장하기 전까지 수식들을 모두 ABC로 옮긴 이후
      # '+'혹은 '-'를 OP에 추가한다.
        while OP and OP[-1] != '(':
            ABC.append(OP.pop())
        OP.append(i)

    elif i == '*' or i == '/':
        while OP and (OP[-1] == '*' or OP[-1] == '/'):
            ABC.append(OP.pop())
        OP.append(i)
    elif i == '(':
        OP.append(i)
    elif i == ')':
        while OP and OP[-1] != '(':
            ABC.append(OP.pop())
        OP.pop()
    else:
        ABC.append(i)
while OP:
    ABC.append(OP.pop())


for i in ABC:
    print(i, end='')
