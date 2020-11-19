import sys
read = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(read())
inOrder = list(map(int, read().split()))
in_location = list(0 for _ in range(n+1))
for i in range(n):
    in_location[inOrder[i]] = i

postOrder = list(map(int, read().split()))
preOrder = []


def find_pre(p_left, p_right, i_left, i_right):
    if p_right-p_left == 0:
        return
    elif p_right-p_left == 1:
        preOrder.append(postOrder[p_left])
        return
    node = postOrder[p_right-1]
    preOrder.append(node)
    node_i = in_location[node]

    find_pre(p_left, p_left-i_left+node_i, i_left, node_i)
    find_pre(node_i+p_right-i_right, p_right-1, node_i+1, i_right)


find_pre(0, n, 0, n)
print(*preOrder)
