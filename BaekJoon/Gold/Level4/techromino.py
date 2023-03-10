import sys
from collections import deque
from itertools import combinations
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(visited, y, x, graph, N, M, cnt):
    if cnt == 4:
        return 0

    answer = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < N and -1 < nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            answer = max(dfs(visited, ny, nx, graph, N, M, cnt + 1)+graph[ny][nx], answer)
            visited[ny][nx] = False
    return answer


def bfs(x, y, q, N, M, graph):
    answer = 0

    check = []
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < N and -1 < nx < M:
            check.append(graph[ny][nx])
    if len(check) > 2:
        for ele in combinations(check, 3):
            answer = max(sum(ele),answer)

    return answer + q[0]



def solution(N, M, graph):

    visited = [[False]*M for _ in range(N)]
    answer = 0

    bfs_answer = 0
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            sub_answer = dfs(visited, i, j, graph, N, M, 1) + graph[i][j]
            answer = max(answer, sub_answer)
            visited[i][j] = False

            q = [graph[i][j]]
            bfs_answer = max(bfs(j, i, q, N, M, graph), bfs_answer)
    return max(answer, bfs_answer)

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N,M,arr))

if __name__ == '__main__':
    main()