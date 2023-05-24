import math
import sys

parent = []


def solution(N, M, graph, plan):
    setParent(N)

    union = set()
    setUnion(N, graph, union)

    calculate(union)
    answer = getAnswer(M, plan)
    print(answer)


def getAnswer(M, plan):
    for i in range(M - 1):
        left = plan[i]
        right = plan[i + 1]
        parent_left = find_parent(left)
        parent_right = find_parent(right)
        if parent_right != parent_left:
            return "NO"
    return "YES"


def calculate(union):
    while union:
        x, y = union.pop()
        parent_x = find_parent(x)
        parent_y = find_parent(y)
        if parent_y != parent_x:
            if parent_x > parent_y:
                parent[parent_y] = parent_x
            else:
                parent[parent_x] = parent_y


def setUnion(N, graph, union):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                if i > j:
                    union.add((i + 1, j + 1))
                else:
                    union.add((j + 1, i + 1))


def find_parent(node):
    start = node
    while node != parent[node]:
        node = parent[node]
    parent[start] = node
    return node


def setParent(N):
    global parent
    parent = [i for i in range(N + 1)]


def main():
    N = int(inputs())
    M = int(inputs())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, inputs().split())))
    plan = list(map(int, inputs().split()))
    solution(N, M, graph, plan)


def inputs():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    main()
