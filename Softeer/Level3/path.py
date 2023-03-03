import sys
import copy

direct = ['>', 'v', '<', '^']
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(graph, visited, x, y, v):
    answer = ''
    # A, 전진
    if -1 < dy[v] * 2 + y < len(graph) and -1 < dx[v] * 2 + x < len(graph[0]) and graph[dy[v] + y][dx[v] + x] == '#' and \
            graph[dy[v] * 2 + y][dx[v] * 2 + x] == '#':
        graph[dy[v] + y][dx[v] + x] = '.'
        graph[dy[v] * 2 + y][dx[v] * 2 + x] = '.'
        answer += dfs(graph, visited, dx[v] * 2 + x, dy[v] * 2 + y, v) + 'A'
    # R:오른쪽
    elif v == 3 and -1 < dy[0] + y < len(graph) and -1 < dx[0] + x < len(graph[0]) and graph[dy[0] + y][dx[0] + x] == '#':
        answer += dfs(graph, visited, x, y, 0) +'R'
        # graph[dy[0] + y][dx[0] + x] = '#'
    elif v < 3 and -1 < dy[v + 1] + y < len(graph) and -1 < dx[v + 1] + x < len(graph[0]) and graph[dy[v + 1] + y][
        dx[v + 1] + x] == '#':
        answer += dfs(graph, visited, x, y, v + 1) +'R'
    # L:왼쪽
    elif v == 0 and -1 < dy[3] + y < len(graph) and -1 < dx[3] + x < len(graph[0]) and graph[dy[3] + y][dx[3] + x] == '#':
        answer += dfs(graph, visited, x, y, 3) +'L'
    elif v > 0 and -1 < dy[v - 1] + y < len(graph) and -1 < dx[v - 1] + x < len(graph[0]) and graph[dy[v - 1] + y][
        dx[v - 1] + x] == '#':
        answer += dfs(graph, visited, x, y, v - 1) + 'L'

    return answer

def check_direct(graph, x, y):
    cnt = 0
    check = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and graph[ny][nx] == '#':
            check = i
            cnt += 1
    if cnt == 1:
        return check
    return 5


def solution(H, W, graph):
    visited = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':
                v = check_direct(graph, j, i)
                if v == 5:
                    continue
                else:
                    answer_direct = direct[v]
                    graph[i][j] = '.'
                    print(i+1,j+1)
                    answer = dfs(graph, visited, j, i, v)
                    print(answer_direct)
                    print(answer[::-1])
                    return


def main():
    H, W = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(H):
        graph.append(list(sys.stdin.readline().split()[0]))
    solution(H, W, graph)


if __name__ == '__main__':
    main()
