import sys
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(N, M, graph):
    visited = [[False]*M for _ in range(N)]
    cnt_graph = [[0]*M for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        (x,y) = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < N and -1 < nx < M:
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    q.append((nx, ny))
                    visited[ny][nx] = True
                if graph[ny][nx] == 1:
                    cnt_graph[ny][nx] += 1
    return cnt_graph


def check_side(cnt_graph, graph, N, M):
    valid = False
    for i in range(N):
        for j in range(M):
            if cnt_graph[i][j] >= 2:
                graph[i][j] = 0
                if not valid:
                    valid = True
    return valid


def solution(N, M, graph):
    answer = 0
    while True:
        cnt_graph = bfs(N,M, graph)
        valid = check_side(cnt_graph, graph, N, M)
        if not valid:
            break
        answer += 1
    return answer


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, M, graph))


if __name__ == '__main__':
    main()