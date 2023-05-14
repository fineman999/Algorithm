import copy
import math
import sys
from collections import deque


dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = math.inf


def find_island(visited, graph, q, N, num):
    global answer
    while q:
        x, y, cnt = q.popleft()

        if cnt > answer:
            return
        if graph[y][x] != 0 and graph[y][x] != num:
            answer = min(answer, cnt - 1)
            return

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < N and not visited[ny][nx] and graph[ny][nx] != num:
                q.append((nx, ny, cnt + 1))
                visited[ny][nx] = True
    return math.inf


def cnt_number(N, graph, q, num):

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < N and graph[ny][nx] == 1:
                graph[ny][nx] = num
                q.append((nx, ny))


def make_number(N, graph):
    num = 2
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                q = deque()
                q.append((j, i))
                graph[i][j] = num
                cnt_number(N, graph, q, num)
                num += 1


def solution(N, graph):
    make_number(N, graph)

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                visited = [[False] * N for _ in range(N)]
                q = deque()
                q.append((j, i, 0))
                visited[i][j] = True
                find_island(visited, graph, q, N, graph[i][j])
    print(answer)



def main():
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, graph)

if __name__ == '__main__':
    main()