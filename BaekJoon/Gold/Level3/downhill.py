import sys
from collections import deque
sys.setrecursionlimit(10**6)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, graph, N, M, visited):
    if x == N - 1 and y == M - 1:
        return 1
    if visited[y][x] != -1:
        return visited[y][x]
    check = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < M and -1 < nx < N and graph[y][x] > graph[ny][nx]:
            check += dfs(nx, ny, graph, N, M, visited)
    visited[y][x] = check

    return visited[y][x]


def solution(M, N, graph):
    q = deque()
    q.append((0, 0))
    visited = [[-1] * N for _ in range(M)]
    answer = dfs(0, 0, graph, N, M, visited)

    print(answer)


def main():
    M, N = inputs()
    graph = []
    for _ in range(M):
        graph.append(list(inputs()))
    solution(M, N, graph)


def inputs():
    return map(int, sys.stdin.readline().rstrip().split())


if __name__ == '__main__':
    main()