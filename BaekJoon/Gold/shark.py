import copy
import math
from collections import deque
import sys


def direction(cnt, x, y, graph, N, q, shark_size):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    check_eat = []
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < N and -1 < nx < N and graph[ny][nx] <= shark_size:
            if 0 < graph[ny][nx] < shark_size:
                check_eat.append((cnt + 1, nx, ny))
            graph[ny][nx] = math.inf
            q.append((cnt + 1, nx, ny))
    return check_eat

def bfs(graph, N, q):
    answer = 0
    shark_size = 2
    shark_eat = 0

    while True:
        new_graph = copy.deepcopy(graph)
        (start_cnt, start_x, start_y) = q[0]
        new_graph[start_y][start_x] = math.inf

        all_eat = []
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0
        while q:
            (cnt, x, y) = q.popleft()
            check_eat = direction(cnt, x, y, new_graph, N, q, shark_size)
            if check_eat:
                all_eat = all_eat + check_eat
        # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
        if len(all_eat) == 0:
            break
        # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
        elif len(all_eat) == 1:
            shark_eat += 1
            (length, nx, ny) = all_eat[0]
            graph[ny][nx] = 0
            answer += length
            q = deque()
            q.append((0, nx, ny))
        # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다
        else:
            #거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
            all_eat.sort(key=lambda x: (x[0], x[2], x[1]))
            shark_eat += 1
            (length, nx, ny) = all_eat[0]
            graph[ny][nx] = 0
            answer += length
            q = deque()
            q.append((0, nx, ny))
    return answer

def solution(N, graph):

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                q = deque()
                graph[i][j] = 0
                q.append((0, j,i))
                return bfs(graph, N, q)



def main():
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for i in range(N):
        graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

    print(solution(N, graph))



if __name__ == "__main__":
    main()