import sys
read=sys.stdin.readline

class Node(object):
    def __init__(self, key, cnt = 0, data = None):
        self.key = key
        self.cnt = cnt
        self.data = data
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.head.cnt = 2

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = Node(char)
                cur_node.cnt += 1
            cur_node = cur_node.child[char]
        cur_node.data = 1

    def check_time(self, string):
        time = 0
        cur_node = self.head
        for char in string:
            if cur_node.cnt != 1 or (cur_node.cnt != 0 and cur_node.data):
                time += 1
            cur_node = cur_node.child[char]


        return time


while True:
    T = Trie()
    try:
        n = int(read())
    except:
        break
      
    input_s = list(list(read().strip()) for _ in range(n))

    for i_s in input_s:
        T.insert(i_s)
    answer = 0
    for i_s in input_s:
        answer += T.check_time(i_s)
    print('%.2f' % (answer/n))

        