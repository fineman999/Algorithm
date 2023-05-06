import sys
from collections import deque

def solution(N, M, graph):
    visited = [[False] * M for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = True

    while q:
        x, y, cnt = q.popleft()
        if x == M - 1 and y == N - 1:
            return cnt

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < M and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((nx, ny, cnt + 1))
    return 0




def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))
    print(solution(N, M, graph))


if __name__ == '__main__':
    main()