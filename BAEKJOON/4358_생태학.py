import sys
read=sys.stdin.readline

class Node(object):
    def __init__(self, key, cnt = 0):
        self.key = key
        self.cnt = cnt
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.child:
                curr_node.child[char] = Node(char)
            curr_node = curr_node.child[char]

        curr_node.cnt += 1

    def check_cnt(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.child:
                return -1
            curr_node = curr_node.child[char]

        if curr_node.cnt:
            return curr_node.cnt
        else:
            return -1


T = Trie()

tree_list = set()
tree_cnt = 0
while 1:
    name = read().strip()
    if not name: break
    tree_list.add(name)
    tree_cnt += 1
    T.insert(name)

tree_list = list(tree_list)
tree_list.sort()
for tree in tree_list:
    print(tree, '%.4f' % ((T.check_cnt(tree)/tree_cnt)*100))
            