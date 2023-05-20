import copy
import sys

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

result = 0
N = 4
DIRECTION_N = 8


def find_fish(graph, fish):
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] == fish:
                return j, i


def move_fish(x, y, graph):
    for fish in range(1, 17):
        position = find_fish(graph, fish)
        if position:
            (x_fish, y_fish) = position
            direct = graph[y_fish][x_fish][1]
            for _ in range(DIRECTION_N):
                nx_fish = x_fish + dx[direct]
                ny_fish = y_fish + dy[direct]
                if -1 < ny_fish < N and -1 < nx_fish < N:
                    if not (ny_fish == y and nx_fish == x):
                        graph[y_fish][x_fish][1] = direct
                        graph[ny_fish][nx_fish], graph[y_fish][x_fish] = graph[y_fish][x_fish], graph[ny_fish][nx_fish]
                        break
                direct = (direct + 1) % DIRECTION_N


def dfs(x, y, answer, graph):
    global result
    result = max(result, answer)
    move_fish(x, y, graph)

    d = graph[y][x][1]

    for _ in range(N - 1):
        x += + dx[d]
        y += + dy[d]
        if -1 < y < N and -1 < x < N and graph[y][x][0] != 0:
            new_graph = copy.deepcopy(graph)
            new_graph[y][x][0] = 0
            dfs(x, y, answer + graph[y][x][0], new_graph)


def solution(graph):
    answer = graph[0][0][0]
    graph[0][0][0] = 0
    dfs(0, 0, answer, graph)

    print(result)


def main():
    graph = []
    for _ in range(4):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        sub_graph = []
        for i in range(0, 8, 2):
            sub_graph.append([tmp[i], tmp[i + 1] - 1])
        graph.append(sub_graph)

    solution(graph)


if __name__ == '__main__':
    main()
