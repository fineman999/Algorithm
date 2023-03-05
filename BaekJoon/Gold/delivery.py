import copy
import math
from collections import deque
from itertools import combinations
import sys


def direction(start, graph, q, x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < len(graph) and -1 < nx < len(graph) and (graph[ny][nx] != -1):
            if graph[ny][nx] == 1:
                answer = math.inf
                for zx, zy in start:
                    check = abs(zx - nx) + abs(zy - ny)
                    if check < answer:
                        answer = check
                cnt += answer
            graph[ny][nx] = -1
            q.append((nx, ny))
    return cnt

def bfs(start, graph, q, M):
    for nx, ny in start:
        graph[ny][nx] = -1
    cnt = 0
    while q:
        (x,y) = q.popleft()
        cnt += direction(start, graph, q, x, y)
    return cnt


def solution(N, M, graph):
    combi = []
    answer = math.inf
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                combi.append((j,i))
    for element in combinations(combi, M):
        new_graph = copy.deepcopy(graph)
        q = deque(element)

        answer = min(answer, bfs(element, new_graph, q, M))

    return answer

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    print(solution(N, M, graph))



if __name__ == "__main__":
    main()