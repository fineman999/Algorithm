import copy
import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def direction(R, C, T, graph, y, x, q):
    weight = graph[y][x]
    cnt = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < R and -1 < nx < C and graph[ny][nx] != -1:
            q.append((nx, ny, weight//5))
            cnt += 1
    q.append((x, y, (weight-(weight//5)*cnt)))


def dust(R, C, T, graph, air):
    visited = [[False]*C for _ in range(R)]
    q = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                direction(R,C,T,graph, i, j, q)
    new_graph = [[0]*C for _ in range(R)]
    # print(q)
    # 처리하기
    while q:
        (x,y, cnt) = q.popleft()
        new_graph[y][x] += cnt
    for a,b in air:
        new_graph[b][a] = -1
    return new_graph


def direction_version_two(R, C, T, graph, y, x, q, weight):
    cnt = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < R and -1 < nx < C and graph[ny][nx] != -1:
            graph[ny][nx] += weight//5
            cnt += 1
    if cnt > 0:
        graph[y][x] += (weight-(weight//5)*cnt)
    else:
        graph[y][x] += weight


def dust_version_two(R, C, T, graph, air):

    q = deque()
    valid = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:

                valid.append((j, i, graph[i][j]))
                graph[i][j] = 0

    while valid:

        (x,y, weight) = valid.popleft()
        direction_version_two(R,C,T,graph, y, x, valid, weight)


def up_test(R, C, T, graph, air):
    [start_x, start_y] = air
    # 1
    graph[start_y-1][start_x] = 0
    for i in range(start_y-1,0,-1):
        graph[i][start_x] = graph[i-1][start_x]

    # 2
    for i in range(C-1):
        graph[0][i] = graph[0][i+1]

    # 3
    for i in range(start_y):
        graph[i][C-1] = graph[i+1][C-1]


    # 4
    for i in range(C-1, 0, -1):
        graph[start_y][i] = graph[start_y][i-1]
    graph[start_y][1] = 0



def down_test(R, C, T, graph, air):
    [start_x, start_y] = air


    # 1
    graph[start_y+1][start_x] = 0
    for i in range(start_y, R-1):
        graph[i][0] = graph[i+1][0]

    # 2
    for i in range(C-1):
        graph[R-1][i] = graph[R-1][i+1]
    # 3
    for i in range(R-1, start_y, -1):
        graph[i][C-1] = graph[i - 1][C-1]

    # 4
    for i in range(C-1, 1, -1):
        graph[start_y][i] = graph[start_y][i-1]
    graph[start_y][1] = 0


def air_test(R, C, T, graph, air):

    up_test(R,C,T,graph,air[0])
    down_test(R,C,T,graph,air[1])



def solution(R, C, T, graph):

    air = []
    for i in range(R):
        if graph[i][0] == -1:
            air.append((0,i))
    # print(air)
    # 1. 미세먼지가 확산된다
    for i in range(T):
        # new_graph = dust(R, C, T, graph, air)
        dust_version_two(R, C, T, graph, air)
        # for ele in new_graph:
        #     print(ele)
        # air_test(R, C, T, new_graph, air)
        # print(graph)
        air_test(R, C, T, graph, air)
        # graph = copy.deepcopy(new_graph)
        # print("after")
        # for ele in graph:
        #     print(ele)
        # print(i)
    answer = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                answer += graph[i][j]
    return answer

def main():
    R, C, T = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(R):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(R, C, T, graph))
        
if __name__ == '__main__':
    main()
        