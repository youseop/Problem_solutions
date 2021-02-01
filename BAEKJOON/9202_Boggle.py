import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
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

        curr_node.data = string

    def search(self, a, b):
        def search_main(node, a, b):
            global score, longest_world, world_cnt, world_length, checklist_world
            
            if node.data:
                world = node.data
                if world in checklist_world:
                    return
                checklist_world.add(world )
                world_len = len(world)
                if world_length < world_len:
                    longest_world = world
                    world_length = world_len
                elif world_length == world_len and world < longest_world:
                    longest_world = world

                world_cnt += 1
                if 3<=world_len<=4:
                    score += 1
                elif world_len == 5:
                    score += 2
                elif world_len == 6:
                    score += 3
                elif world_len == 7:
                    score += 5
                elif world_len == 8:
                    score += 11
                return
            for x,y in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
                ax, by = a+x, b+y
                if 0<=ax<4 and 0<=by<4 and visit[ax][by] and board[ax][by] in node.child:
                    visit[ax][by] = 0
                    curr_node = node.child[board[ax][by]]
                    search_main(curr_node, ax, by)
                    visit[ax][by] = 1

        curr_node = self.head
        visit = list(list(1 for _ in range(4)) for _ in range(4))
        visit[a][b] = 0
        search_main(curr_node, a, b)


        


T = Trie()
for _ in range(int(read())):
    T.insert(read().strip())

read()

for _ in range(int(read())):
    board = list(list(read().strip()) for _ in range(4))
    score = 0
    longest_world = ""
    world_cnt = 0
    world_length = 0
    checklist_world = set()
    for i in range(4):
        for j in range(4):
            T.search(i,j)
    print(score,longest_world,world_cnt)
    read()