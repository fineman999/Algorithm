import copy
import sys
from collections import deque
sys.setrecursionlimit(2500)

def direction(x, y, q, graph):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < len(graph) and -1 < nx < len(graph[ny]) and graph[ny][nx] == 0:
            # visited[ny][nx] = True
            graph[ny][nx] = 1
            q.append((nx, ny))



def bfs(q, graph):

    valid = False
    result = 0

    if len(q) > 0:
        valid = True
    while valid:
        new_q = deque()
        while q:
            (x, y) = q.popleft()
            direction(x, y, new_q, graph)
        if len(new_q) == 0:
            valid = False
            break
        q = copy.deepcopy(new_q)
        result += 1

    return result





def solution(M, N, graph):

    q = deque()


    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append((j, i))


    result = bfs(q,graph)
    # print(graph)
    if any(0 in i for i in graph):
        return -1
    return result

def main():
    M, N = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    print(solution(M, N, graph))
if __name__ == "__main__":
    main()