import math
import copy

def floyd_warshall(graph, n: int, results: list):
    # 1 자기 자신 0 세팅
    for i in range(len(graph)):
        graph[i][i] = 0

    # 세팅
    for start, end in results:
        graph[end][start] = 1

    # 점화식 계산
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def solution(n, results):
    graph = [[math.inf] * (n + 1) for _ in range(n + 1)]
    floyd_warshall(graph, n + 1, results)
    result = 0
    for i in range(1, n + 1):
        answer = 0
        for j in range(1, n + 1):
            if graph[i][j] != math.inf and graph[i][j] != 0:
                answer += 1
            if graph[j][i] != math.inf and graph[j][i] != 0:
                answer += 1
        if answer == n-1:
            result += 1
    return result
def main():
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


if __name__ == "__main__":
    main()