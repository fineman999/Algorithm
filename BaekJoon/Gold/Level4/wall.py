import math
import sys
from collections import deque


def bfs(N, M, q, graph):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[math.inf]*M for _ in range(N)]
    broken = [[True]*M for _ in range(N)]
    visited[0][0] = 1
    while q:
        (x, y, valid) = q.popleft()
        # 도착했을 경우가 제일 빠른 경우이므로 리턴
        if x == M-1 and y == N-1:
            return visited[N-1][M-1]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < M:
                if visited[y][x] + 1 < visited[ny][nx]:
                    # 기본 벽이 아닐 경우
                    if graph[ny][nx] == '0':
                        visited[ny][nx] = visited[y][x] + 1
                        broken[ny][nx] = valid
                        q.append((nx, ny, valid))
                    else:
                        # 벽이고 아직까지 벽 부수기를 사용하지 않은 경우
                        if valid:
                            visited[ny][nx] = visited[y][x] + 1
                            broken[ny][nx] = False
                            q.append((nx, ny, False))
                # 아직까지 벽 부수기를 사용하지 않은 값을 큐에 넣기
                if valid and not broken[ny][nx]:
                    if graph[ny][nx] == '0':
                        visited[ny][nx] = visited[y][x] + 1
                        broken[ny][nx] = valid
                        q.append((nx, ny, valid))

    if visited[N-1][M-1] == math.inf:
        return -1
    return visited[N-1][M-1]



def solution(N, M, graph):
    q = deque()
    q.append((0, 0, True))

    answer = bfs(N, M, q, graph)
    print(answer)



def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(N):
        graph.append(list(sys.stdin.readline().rstrip()))
    solution(N, M, graph)

if __name__ == '__main__':
    main()