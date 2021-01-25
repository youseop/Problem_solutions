import sys
read=sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = Node(char)
            cur_node = cur_node.child[char]

        cur_node.data = string

    def search(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.child:
                return False
            cur_node = cur_node.child[char]

        if cur_node.data:
            return True
        return False

n,m = map(int,read().split())

input_s = list(list(read().strip()) for _ in range(n))
check_s = list(list(read().strip()) for _ in range(m))
T = Trie()
for i_s in input_s:
    T.insert(i_s)

cnt = 0
for c_s in check_s:
    if T.search(c_s):
        cnt += 1
print(cnt)