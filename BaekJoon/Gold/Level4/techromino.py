import sys
from collections import deque
from itertools import combinations
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0
max_element = 0
def dfs(visited, y, x, graph, N, M, cnt, result):
    global answer
    if result + max_element*(4-cnt) < answer:
        return
    if cnt == 4:
        answer = max(answer, result)
        return

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < N and -1 < nx < M and not visited[ny][nx]:
            if cnt == 2:
                visited[ny][nx] = True
                dfs(visited, y, x, graph, N, M, cnt + 1, result + graph[ny][nx])
                visited[ny][nx] = False

            visited[ny][nx] = True
            dfs(visited, ny, nx, graph, N, M, cnt + 1, result + graph[ny][nx])
            visited[ny][nx] = False




def solution(N, M, graph):

    visited = [[False]*M for _ in range(N)]
    global max_element
    max_element = max(map(max,graph))
    # print(max_element)
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(visited, i, j, graph, N, M, 1, graph[i][j])
            visited[i][j] = False
    return answer

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N,M,arr))

if __name__ == '__main__':
    main()