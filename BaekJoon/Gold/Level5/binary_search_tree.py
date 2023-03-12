import sys
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None



class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_node(self.root, data)
        return self.root is not None

    def _insert_node(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if node.data >= data:
                node.left = self._insert_node(node.left, data)
            else:
                node.right = self._insert_node(node.right, data)

        return node

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node.left:
            self._postorder(node.left)
        if node.right:
            self._postorder(node.right)
        print(node.data)


def get_postorder(arr):

    if len(arr) <= 1:
        return arr
    # print(arr)
    root = arr[0]

    for i in range(1, len(arr)):
        if root < arr[i]:
            return get_postorder(arr[1:i]) + get_postorder(arr[i:]) + [root]
    return get_postorder(arr[1:]) + [root]



def solution(arr):

    # Tree로 시간 초과
    # tree = BinaryTree()
    # for ele in arr:
    #     tree.insert(ele)
    # tree.postorder()

    answer = get_postorder(arr)
    for ele in answer:
        print(ele)


def main():
    arr = []

    while True:
        try:
            arr.append(int(sys.stdin.readline()))
        except:
            break
    solution(arr)

if __name__ == '__main__':
    main()
