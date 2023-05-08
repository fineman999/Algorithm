import math
import sys
import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(visited, n, graph):
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    visited[0][0] = graph[0][0]
    while q:
        (dist, x, y) = heapq.heappop(q)
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < n and -1 < nx < n and visited[y][x] + graph[ny][nx] < visited[ny][nx]:
                visited[ny][nx] = graph[ny][nx] + dist
                heapq.heappush(q, (visited[ny][nx], nx, ny))
    return visited[n-1][n-1]


def solution(n, graph):
    visited = [[math.inf] * n for _ in range(n)]
    return bfs(visited, n, graph)


def main():
    cnt = 1
    while True:
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            break
        graph = []
        for i in range(n):
            graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
        answer = solution(n, graph)
        print(f"Problem {cnt}: {answer}")
        cnt += 1


if __name__ == '__main__':
    main()

