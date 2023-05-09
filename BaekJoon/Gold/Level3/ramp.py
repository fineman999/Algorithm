import sys


def check_left(N, L, graph):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        valid = True
        for j in range(1, N):
            if graph[i][j-1] > graph[i][j]:
                if abs(graph[i][j-1] - graph[i][j]) == 1:
                    tmp = graph[i][j]
                    for k in range(j, j + L):
                        if k >= N or graph[i][k] != tmp or visited[i][k]:
                            valid = False
                            break
                        else:
                            visited[i][k] = True
                else:
                    valid = False
                    break
            if graph[i][j-1] < graph[i][j]:
                tmp = graph[i][j-1]
                if abs(graph[i][j-1] - graph[i][j]) == 1:
                    for k in range(j-1, j-1-L, -1):
                        if k<= -1 or graph[i][k] != tmp or visited[i][k]:
                            valid = False
                            break
                        else:
                            visited[i][k] = True
                else:
                    valid = False
                    break
        if valid:
            cnt += 1
    return cnt


def check_right(N, L, graph):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for j in range(N):
        valid = True
        for i in range(1, N):
            if graph[i-1][j] > graph[i][j]:
                if abs(graph[i-1][j] - graph[i][j]) == 1:
                    tmp = graph[i][j]
                    for k in range(i, i + L):
                        if k >= N or graph[k][j] != tmp or visited[k][j]:
                            valid = False
                            break
                        else:
                            visited[k][j] = True
                else:
                    valid = False
                    break

            if graph[i-1][j] < graph[i][j]:
                if abs(graph[i-1][j] - graph[i][j]) == 1:
                    tmp = graph[i-1][j]
                    for k in range(i-1, i-1-L, -1):
                        if k <= -1 or graph[k][j] != tmp or visited[k][j]:
                            valid = False
                            break
                        else:
                            visited[k][j] = True
                else:
                    valid = False
                    break
        if valid:
            cnt += 1
    return cnt


def solution(N, L, graph):
    row_cnt = check_left(N, L, graph)
    col_cnt = check_right(N, L, graph)
    print(row_cnt+ col_cnt)


def main():
    N, L = inputs()
    graph = []
    for _ in range(N):
        graph.append(list(inputs()))
    solution(N, L, graph)


def inputs():
    return map(int, sys.stdin.readline().rstrip().split())


if __name__ == '__main__':
    main()