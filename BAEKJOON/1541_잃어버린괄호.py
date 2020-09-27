string = input().split('-')
for i in range(len(string)):
    if '+' in string[i]:
        tmp = string[i].split('+')
        sum = 0
        for x in tmp:
            sum += int(x)
        string[i] = sum
    else:
        string[i] = int(string[i])

answer = string[0]
for num in string[1:]:
    answer -= num
print(answer)
