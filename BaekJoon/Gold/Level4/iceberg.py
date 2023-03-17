import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(graph, q, visited, N, M, change):

    while q:
        (x,y) = q.popleft()
        cnt = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < M and graph[ny][nx] == 0:
                cnt += 1
        if cnt > 0:
            change.append((x, y, cnt))

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < M and graph[ny][nx] > 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))


def recursive(N, M, graph):
    answer = 0
    while True:
        visited = [[False] * M for _ in range(N)]
        cnt_iceberg = 0
        change = deque()
        for i in range(N):
            for j in range(M):
                if graph[i][j] > 0 and not visited[i][j]:
                    # print(i,j)
                    q = deque()
                    q.append((j, i))
                    visited[i][j] = True
                    bfs(graph, q, visited, N, M, change)
                    cnt_iceberg += 1

        if cnt_iceberg > 1:
            return answer
        elif cnt_iceberg == 0:
            return 0
        answer += 1
        while change:
            (x, y, cnt) = change.popleft()
            if graph[y][x] < cnt:
                graph[y][x] = 0
            else:
                graph[y][x] -= cnt




def solution(N, M, graph):

    answer = recursive(N, M, graph)
    print(answer)


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, M, graph)


if __name__ == '__main__':
    main()