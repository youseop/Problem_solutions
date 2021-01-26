import sys
read=sys.stdin.readline

def traverse_main(node,depth):
    children = list((node.child).keys())
    children.sort()
    for c in children:
        for _ in range(depth):
            print('--',end='')
        print(c)
        traverse_main(node.child[c],depth+1)

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, strings):
        curr_node = self.head
        for string in strings:
            if string not in curr_node.child:
                curr_node.child[string] = Node(string)
            curr_node = curr_node.child[string]

    def traverse(self):
        curr_node = self.head
        traverse_main(curr_node ,0)

T = Trie()
for _ in range(int(read())):
    _, *strings = read().split()
    T.insert(strings)

T.traverse()