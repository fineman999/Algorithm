import copy
import sys
from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(q, graph, visited, N, target):

    while q:
        (x,y) = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if -1 < ny < N and -1 < nx < N and not visited[ny][nx] and graph[ny][nx] in target:
                q.append((nx, ny))
                visited[ny][nx] = True


def solution(N, graph):

    left = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and (graph[i][j] == 'R' or graph[i][j] == 'B' or graph[i][j] == 'G'):
                q = deque()
                q.append((j, i))
                visited[i][j] = True
                target = [graph[i][j]]
                bfs(q, graph, visited, N, target)
                left += 1


    right = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and (graph[i][j] == 'R' or graph[i][j] == 'B' or graph[i][j] == 'G'):
                q = deque()
                q.append((j, i))
                visited[i][j] = True
                if graph[i][j] =='R' or graph[i][j] == 'G':
                    target = ['R', 'G']
                else:
                    target = ['B']
                bfs(q, graph, visited, N, target)
                right += 1
    print(left, right)

def main():
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(sys.stdin.readline().rstrip().split()[0]))
    solution(N, graph)

if __name__ == '__main__':
    main()