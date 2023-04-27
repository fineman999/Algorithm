import sys

parent = []
def find_parent(node):
    start = node
    while node != parent[node]:
        node = parent[node]
    parent[start] = node
    return node

def merge(x, y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)
    if parent_x == parent_y:
        return False
    if parent_x > parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y
    return True

def solution(graph, N, M):
    global parent
    parent = [i for i in range(N+1)]
    graph.sort(key = lambda x:x[0])
    tmp = 0
    cnt = 0
    for i in range(M):
        if cnt == N-2:
            break
        c, a, b = graph[i]
        if merge(a, b):
            tmp += c
            cnt += 1
    print(tmp)


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(M):
        a,b,c = list(map(int, sys.stdin.readline().rstrip().split()))
        graph.append([c, b, a])
    solution(graph, N, M)


if __name__ == '__main__':
    main()