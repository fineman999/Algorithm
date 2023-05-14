import copy
import math
import sys
from collections import deque


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def find_island(visited, graph, q, N):
    legs = deque()
    new_visited = copy.deepcopy(visited)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < N and visited[ny][nx] == math.inf:

                if graph[ny][nx] == 1:
                    q.append((nx, ny))
                    visited[ny][nx] = -1
                    new_visited[ny][nx] = -1
                else:
                    legs.append((nx, ny))
                    new_visited[ny][nx] = 1

    return legs, new_visited


def find_min_dist(legs, visited, graph, N):
    # for ele in visited:
    #     print(ele)
    # print()
    while legs:
        x, y = legs.popleft()

        if graph[y][x] == 1:
            return visited[y][x] - 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < N and visited[y][x] + 1 < visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                legs.append((nx, ny))

    return math.inf

def solution(N, graph):

    visited = [[math.inf] * N for _ in range(N)]
    answer = math.inf
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == math.inf:
                q = deque()
                q.append((j, i))
                visited[i][j] = -1
                legs, new_visited = find_island(visited, graph, q, N)
                answer = min(find_min_dist(legs, new_visited, graph, N), answer)

    print(answer)



def main():
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, graph)

if __name__ == '__main__':
    main()