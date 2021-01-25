import sys
read=sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self,string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            elif curr_node.children[char].data:
                return 1
            curr_node = curr_node.children[char]

        curr_node.data = string

        return 0


for _ in range(int(read())):
    T = Trie()
    nums = list(list(read().strip()) for _ in range(int(read())))
    nums.sort(key = lambda x: len(x))
    for num in nums:
        if T.insert(num):
            print('NO')
            break
    else:
        print('YES')