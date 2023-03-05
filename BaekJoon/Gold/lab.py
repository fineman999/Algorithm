import math
import sys, copy
from collections import deque

result = math.inf

answer = 0
def direction(q, x, y, graph):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1< ny < len(graph) and -1 < nx < len(graph[0]) and graph[ny][nx] == 0:
            graph[ny][nx] = 2
            cnt += 1
            q.append((nx, ny))
    return cnt


def bfs(graph, q, virus):
    cnt = virus
    global result

    while q:
        (x,y) = q.popleft()
        cnt += direction(q, x, y, graph)
        if cnt > result:
            return

    if cnt < result:
        global answer
        answer = 0
        for i in graph:
            answer += i.count(0)
        result = cnt


def wall(N, M, graph, cnt, q, start):
    if cnt == 3:
        new_graph= copy.deepcopy(graph)
        new_q = copy.deepcopy(q)
        bfs(new_graph, new_q, len(q))
        return
    # for i in range(x, N):
    #     for j in range(y, M):
    #         if graph[i][j] == 0:
    #             graph[i][j] = 1
    #             wall(N, M, graph, cnt + 1, q, i, j)
    #             graph[i][j] = 0
    for i in range(start, N*M):
        x = int(i%M)
        y = int(i/M)
        if graph[y][x] == 0:
            graph[y][x] = 1
            wall(N, M, graph, cnt + 1, q, i + 1)
            graph[y][x] = 0




def solution(N, M, graph):
    arr = []
    q = deque()
    # for i in range(0, N*M):
    #     x = int(i%M)
    #     y = int(i/M)
    #     print(i, x, y)
    #     print(graph[y][x])

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                q.append((j,i))

    wall(N, M, graph, 0, q,0)

    return answer

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    print(solution(N, M, graph))



if __name__ == "__main__":
    main()