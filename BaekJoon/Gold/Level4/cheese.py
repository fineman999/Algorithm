import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(q, graph, N, M):
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < M:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 2
                    q.append((nx, ny))
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 3


def check(graph, N, M):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return j, i
    return -1, -1

def check_cnt(graph, N, M):
    cnt = 0
    for k in range(N):
        for h in range(M):
            if graph[k][h] != 1:
                graph[k][h] = 0
            else:
                cnt += 1
    return cnt

def recursive(graph, N, M):

    answer = []
    x, y = check(graph, N, M)
    if x == -1 and y == -1:
        return
    q = deque()
    q.append((x, y))
    graph[y][x] = 2
    bfs(q, graph, N, M)
    cnt = check_cnt(graph, N, M)
    if cnt > 0:
        answer += recursive(graph, N, M) + [cnt]
    return answer


def solution(N, M, graph):

    cnt = check_cnt(graph, N, M)
    answer = []
    if cnt > 0:
        answer += recursive(graph, N, M) + [cnt]
    if answer ==[]:
        print(0)
        print(0)
        return
    print(len(answer))
    print(answer[0])



def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, M, graph)


if __name__ == '__main__':
    main()