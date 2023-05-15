import sys
sys.setrecursionlimit(10**6)

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def dfs(y, x, N, visited, graph):
    if visited[y][x] > 0:
        return visited[y][x]

    valid = True
    answer = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < N and -1 < nx < N and graph[y][x] < graph[ny][nx]:
            answer = max(dfs(ny, nx, N, visited, graph), answer)
            valid = False

    if valid:
        visited[y][x] = 1
        return 1

    visited[y][x] = answer + 1
    return answer + 1


def solution(N, graph):
    visited = [[0] * N for _ in range(N)]

    answer = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = dfs(i, j, N, visited, graph)
                answer = max(answer, visited[i][j])
    print(answer)


def main():
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, graph)


if __name__ == '__main__':
    main()