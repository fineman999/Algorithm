import math
import copy

def floyd_warshall(graph, n: int, results: list):
    # 1 자기 자신 0 세팅
    for i in range(len(graph)):
        graph[i][i] = 0

    win_graph = copy.deepcopy(graph)
    lose_graph = copy.deepcopy(graph)
    # 세팅
    for result in results:
        [a, b] = result
        win_graph[b][a] = 1
        lose_graph[a][b] = 1

    # 점화식 계산
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                win_graph[i][j] = min(win_graph[i][j], win_graph[i][k] + win_graph[k][j])
                lose_graph[i][j] = min(lose_graph[i][j], lose_graph[i][k] + lose_graph[k][j])

    for i in range(len(lose_graph)):
        for j in range(len(lose_graph[i])):
            graph[i][j] = min(lose_graph[i][j], win_graph[i][j])


def solution(n, results):
    graph = [[math.inf] * (n + 1) for _ in range(n + 1)]
    floyd_warshall(graph, n + 1, results)
    answer = 0
    for i in range(1, n + 1):
        if math.inf not in graph[i][1:]:
            answer += 1

    return answer


def main():
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


if __name__ == "__main__":
    main()
