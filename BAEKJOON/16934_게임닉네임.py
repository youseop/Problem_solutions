import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

class Node(object):
    def __init__(self, key, cnt=0, data=None):
        self.key = key
        self.cnt = cnt
        self.data = data
        self.child = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        flag = 1
        curr_node = self.head
        for char in string:
            if flag:
                print(char,end='')
            if char not in curr_node.child:
                curr_node.child[char] = Node(char)
                flag = 0          
                
            curr_node = curr_node.child[char]
    
        if curr_node.cnt:
            print(curr_node.cnt+1,end='')
        
        curr_node.cnt += 1
        print()

T = Trie()
for _ in range(int(read())):
    name = read().strip()
    T.insert(name)