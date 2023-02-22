import sys
sys.setrecursionlimit(10**6)

answer_preorder = []
answer_postorder = []


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            (now_data, now_x, now_y) = data
            (before_data, before_x, before_y) = node.data
            if before_x > now_x:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        answer_preorder.append(node.data[0])
        if node.left:
            self._preorder(node.left)
        if node.right:
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node.left:
            self._postorder(node.left)
        if node.right:
            self._postorder(node.right)
        answer_postorder.append(node.data[0])


def solution(nodeinfo):
    bst = BinarySearchTree()
    diary = {tuple(check): index + 1 for index, check in enumerate(nodeinfo)}
    nodeinfo.sort(key=lambda x: (x[1], -x[0]), reverse=True)

    for element in nodeinfo:
        insert_node = (diary[tuple(element)], element[0], element[1])
        bst.insert(insert_node)
    bst.preorder()
    bst.postorder()
    return [answer_preorder, answer_postorder]

def main():
    print(solution(	[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))

if __name__ == "__main__":
    main()