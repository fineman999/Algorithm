import sys
from collections import deque
# 1: 익은 토마토, 0: 익지 않은 토마토 -1: 토마토가 들어있지 않음
di = [0,1,0,-1,0,0]
dj = [1,0,-1,0,0,0]
dk = [0,0,0,0,1,-1]
def bfs(graph, M, N, H, q, visited):
    while q:
        (k, i, j) = q.popleft()
        for y in range(6):
            ni = di[y] + i
            nj = dj[y] + j
            nk = dk[y] + k
            if -1 < nk < H and -1 < ni < N and -1 < nj < M and visited[nk][ni][nj] == -1 and graph[nk][ni][nj] == 0:
                visited[nk][ni][nj] = visited[k][i][j] + 1
                q.append((nk, ni, nj))
    # return visited



def solution(graph, M, N, H):
    q = deque()
    visited = []
    for k in range(H):
        temp = [[-1]*M for _ in range(N)]
        visited.append(temp)
    # print(visited)
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if graph[k][i][j] == 1:
                    q.append((k, i, j))
                    visited[k][i][j] = 0
    # print(visited)
    bfs(graph, M, N, H, q, visited)
    answer = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if visited[k][i][j] == -1 and graph[k][i][j] != -1:
                    return -1
                if graph[k][i][j] != -1:
                    answer = max(answer, visited[k][i][j])
    return answer




def main():
    M, N, H = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for i in range(H):
        temp = []
        for j in range(N):
            temp.append(list(map(int, sys.stdin.readline().rstrip().split())))
        graph.append(temp)
    print(solution(graph, M, N, H))

if __name__ == '__main__':
    main()
