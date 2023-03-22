import sys
from collections import defaultdict

width = 1

graph = defaultdict(list)
diary = defaultdict(list)
parent = defaultdict(int)
def recursive(node, height):
    global width
    [left, right] = graph[node]

    if left != -1:
        recursive(left, height + 1)
    # print(node, height)

    if height not in diary:
        diary[height] = [width, width]
    else:
        diary[height][0] = min(diary[height][0], width)
        diary[height][1] = max(diary[height][1], width)

    width += 1
    if right != -1:
        recursive(right, height + 1)


def find_parent(node):
    while 0 != node:
        if parent[node] == 0:
            break
        node = parent[node]
    return node


def solution(N, nodes):
    global graph, diary
    for root, a, b in nodes:
        graph[root] = [a, b]
        parent[a] = root
        parent[b] = root
    # print(parent)
    # 1. 루트 노드 찾기
    root = find_parent(-1)

    # 2. 중위 순회 실행
    recursive(root, 1)

    # 3. 결과 값 찾기
    result = list(diary.items())
    result.sort()
    (height, [left, right]) = result[0]
    answer = [left, right, height]
    for element in result:
        (height, [left, right]) = element
        # print(height, left, right)
        if (right - left + 1) > (answer[1] - answer[0] + 1):
            answer = [left, right, height]
    return answer


def main():
    N = int(sys.stdin.readline().rstrip())
    nodes = []
    for _ in range(N):
        nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))
    answer = solution(N, nodes)
    print(answer[2], answer[1] - answer[0] + 1)


if __name__ == '__main__':
    main()
