
def solution(words, queries):
    class Node(object):
        def __init__(self, key, data=None):
            self.key = key
            self.data = {}
            self.children = {}

    class Trie(object):
        def __init__(self):
            self.head = Node(None)

        def insert(self, string):
            curr_node = self.head
            length = len(string)

            if length in curr_node.data:
                curr_node.data[length] += 1
            else:
                curr_node.data[length] = 1

            for char in string:
                if char not in curr_node.children:
                    curr_node.children[char] = Node(char)
                curr_node = curr_node.children[char]
                if length in curr_node.data:
                    curr_node.data[length] += 1
                else:
                    curr_node.data[length] = 1

        def search(self, string, length):
            curr_node = self.head
            for char in string:
                if char in curr_node.children:
                    curr_node = curr_node.children[char]
                else:
                    return 0
            if length in curr_node.data:
                return curr_node.data[length]
            else:
                return 0

    answer = []
    words_left = Trie()
    words_right = Trie()
    for w in words:
        words_right.insert(w)
        words_left.insert(w[::-1])

    for q in queries:
        length = len(q)
        left = True
        if q[-1] == "?":
            left = False
        q = q.strip("?")
        if left:
            q = q[::-1]
            answer.append(words_left.search(q, length))
        else:
            answer.append(words_right.search(q, length))
    return answer
