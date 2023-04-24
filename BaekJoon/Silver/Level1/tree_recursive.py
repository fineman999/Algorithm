import sys
from collections import defaultdict


def preorder(diary, root):
    print(root, end='')
    if diary[root][0] != '.':
        preorder(diary, diary[root][0])
    if diary[root][1] != '.':
        preorder(diary, diary[root][1])

def inorder(diary, root):

    if diary[root][0] != '.':
        inorder(diary, diary[root][0])
    print(root, end='')
    if diary[root][1] != '.':
        inorder(diary, diary[root][1])

def postorder(diary, root):
    if diary[root][0] != '.':
        postorder(diary, diary[root][0])
    if diary[root][1] != '.':
        postorder(diary, diary[root][1])
    print(root, end='')


def solution(diary):
    preorder(diary, 'A')
    print()
    inorder(diary, 'A')
    print()
    postorder(diary, 'A')
    #


def main():
    N = int(sys.stdin.readline().rstrip())
    diary = defaultdict(list)
    for _ in range(N):
        a, b, c = sys.stdin.readline().rstrip().split()
        diary[a] = [b, c]
    solution(diary)

if __name__ == '__main__':
    main()

