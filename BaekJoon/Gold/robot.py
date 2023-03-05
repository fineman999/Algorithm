import copy
import math
from collections import deque
import sys


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# d == 0: 북 1: 동, 2: 남 3: 서
def direction(graph, start):
    [y, x, d] = start
    i = d
    for _ in range(4):
        i = (i + 3)%4
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and graph[ny][nx] == 0:
            return False
    return True

result = 0
def dfs(graph, start):
    [y, x, d] = start
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

    if graph[y][x] == 0:
        global result
        result += 1
        graph[y][x] = 2

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if direction(graph, start):
        # 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        ny = y+dy[(d+2)%4]
        nx = x+dx[(d+2)%4]
        if -1< ny < len(graph) and -1 < nx < len(graph[0]) and graph[ny][nx] == 1:
            return

        dfs(graph, [ny, nx, d])
        # 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        # elif -1 < ny < len(graph) and -1 < nx < len(graph[0]) and graph[ny][nx] == 1:
        # #     print(graph[ny][nx], ny, nx)

    else:
        new_d = (d+3)%4
        ny = y+dy[new_d]
        nx = x+dx[new_d]
        if -1< ny < len(graph) and -1 < nx < len(graph[0]) and graph[ny][nx] == 0:
            dfs(graph, [ny, nx, new_d])
        else:
            dfs(graph, [y, x, new_d])


def solution(N, M, graph, start):
    [r,c,d]=start
    # check = [r-1,c-1,d]
    dfs(graph, start)
    cnt = 0

    return result

def main():
    N, M = map(int, sys.stdin.readline().split())
    start = list(map(int, sys.stdin.readline().split()))
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    print(solution(N, M, graph, start))



if __name__ == "__main__":
    main()