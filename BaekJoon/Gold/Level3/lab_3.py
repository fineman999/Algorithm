import math
import sys
from itertools import combinations
from collections import deque
answer = math.inf
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(n, graph, q, visited):
    global answer
    sub_answer = 0

    while q:
        (x, y, cnt) = q.popleft()
        if graph[y][x] != 2:
            sub_answer = cnt
        if sub_answer >= answer:
            return
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < n and -1 < nx < n and not visited[ny][nx]:
                if graph[ny][nx] == 0 or graph[ny][nx] == 2:
                    q.append((nx, ny, cnt + 1))
                    visited[ny][nx] = True

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and not visited[i][j]:
                return

    answer = min(answer, sub_answer)


def solution(n, graph, m):
    virus = []
    set_virus(graph, n, virus)
    for ele in combinations(virus, m):
        q = deque()
        visited = [[False] * n for _ in range(n)]
        for x,y in ele:
            q.append((x,y, 0))
            visited[y][x] = True
        bfs(n, graph, q, visited)

    if answer == math.inf:
        return -1
    return answer


def set_virus(graph, n, virus):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                virus.append((j, i))


def main():
    n, m = inputs()
    graph = []
    for _ in range(n):
        graph.append(list(inputs()))
    result = solution(n, graph, m)
    print(result)


def inputs():
    return map(int, sys.stdin.readline().rstrip().split())


if __name__ == '__main__':
    main()