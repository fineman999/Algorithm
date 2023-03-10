import sys
from collections import defaultdict

def solution_two(phone_book):
    key_value_dict = defaultdict(str)
    phone_book.sort()
    for element in phone_book:
        for i in range(len(element)):
            if element[:i+1] in key_value_dict:
                return "NO"
        key_value_dict[element] = 1
    return "YES"
# key - 값으로 입력될 문자
# data - 문자열의 종료를 알리는 flag
# children - 자식노드를 저장
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        current_node = self.root

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.root
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            print(current_node.data)
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.root
        words = []
        for p in prefix:

            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None
        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        return words


def solution(n, phones):
    phones.sort(reverse=True)
    # print(phones)
    trie = Trie()
    for phone in phones:
        if trie.starts_with(phone) is None:
            # print(phone)
            trie.insert(phone)
        else:
            return "NO"
        # print()
    # print(trie.search('97625999'))
    return "YES"




def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        phones = []
        for i in range(n):
            phones.append(sys.stdin.readline().rstrip())
        # print(solution(n, phones))
        print(solution_two(phones))
if __name__ == '__main__':
    main()