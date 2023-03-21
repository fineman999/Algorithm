import sys
sys.setrecursionlimit(10**6)
inorder = []
postorder = []
diary = {}
def make_preorder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):  # 둘 중 하나라도 조건이 빠져있으면 무한루프 돌 수 있음
        return

    root = postorder[post_end]  # 후위순회의 끝값 == 루트
    left_len = diary[root] - in_start  # 루트의 중위순회 인덱스 - 중위순회 시작점 == 왼쪽 노드 길이
    print(root, end=" ")  # 전위순회에서는 루트가 먼저 출력되어야 하니까 먼저 출력하고 빠지기
    make_preorder(in_start, in_start+left_len-1, post_start, post_start+left_len-1) # 왼쪽 노드
    make_preorder(in_start+left_len+1, in_end, post_start+left_len, post_end-1) # 오른쪽 노드



def solution(n):
    global diary
    diary = {inorder[i] : i for i in range(n)}

    make_preorder(0, n-1, 0, n-1)




def main():
    global inorder
    global postorder
    n = int(sys.stdin.readline().rstrip())
    inorder = list(map(int, sys.stdin.readline().rstrip().split()))
    postorder = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n)


if __name__ == '__main__':
    main()
