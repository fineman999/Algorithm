import sys


def solution(n, preorder, inorder):
    diary = {inorder[i]: i for i in range(len(inorder))}
    answer = []

    def recursive(start_in, end_in, start_pre, end_pre):
        if start_in > end_in or start_pre > end_pre:
            return
        root = preorder[start_pre]
        index = diary[root] - start_in
        recursive(start_in, start_in + index - 1, start_pre + 1, start_pre + index)
        recursive(start_in + index + 1, end_in, start_pre + index + 1, end_pre)
        answer.append(str(root))
        # print(root, end=' ')

    recursive(0, n - 1, 0, n - 1)
    return answer


def main():
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())
        preorder = list(map(int, sys.stdin.readline().rstrip().split()))
        inorder = list(map(int, sys.stdin.readline().rstrip().split()))
        answer.append(solution(n, preorder, inorder))
    for ele in answer:
        print(" ".join(ele))


if __name__ == '__main__':
    main()
