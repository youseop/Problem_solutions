import sys
read = sys.stdin.readline

# 아래의 Node, Trie class는
# [https://alpyrithm.tistory.com/74]
# 알파이님의 블로그를 토대로 작성했습니다.


class Node(object):
    # trie 자료구조를 위한 node
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        # dictionary 자료구조 사용
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 해당 노드로 이동
            curr_node = curr_node.children[char]

        curr_node.data = string

    # 문자열이 존재하는지 search
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.data != None:
            return True


n, m = map(int, read().split())

word_trie = Trie()
word_len = list(False for _ in range(501))
# 주어진 문자열과 길이가 같은 문자열에 대해서만 탐색을 진행해
# 시간복잡도 줄이기 위함

for _ in range(n):
    word = read().strip()
    word_trie.insert(word)
    word_len[len(word)] = True
cnt = 0
for _ in range(m):
    word = read().strip()
    if word_len[len(word)] and word_trie.search(word):
        cnt += 1

print(cnt)
