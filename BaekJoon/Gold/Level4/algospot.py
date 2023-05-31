import math
import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(N, M, graph, visited, q):
    while q:
        (x, y) = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < M and visited[ny][nx] == math.inf:
                if graph[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))
                else:
                    visited[ny][nx] = visited[y][x]
                    q.appendleft((nx, ny))



def solution(N, M, graph):
    visited = [[math.inf] * M for _ in range(N)]

    q = deque()
    if graph[0][0] == 0:
        visited[0][0] = 0
    else:
        visited[0][0] = 1
    q.append((0, 0))

    bfs(N, M, graph, visited, q)

    print(visited[-1][-1])

def main():
    M, N = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))
    solution(N, M, graph)


if __name__ == '__main__':
    main()
