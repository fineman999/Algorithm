import math


def floyd_warshall(graph: list, n: int, fares: list):
    # 1. 자기자신 0으로 세팅
    for i in range(n+1):
        graph[i][i] = 0

    # 2. 초기 값 세팅
    for fare in fares:
        [c, d, f] = fare
        graph[c][d] = f
        graph[d][c] = f

    # 3. 점화식 계산
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


def calculate(graph: list, n: int, s: int, a: int, b: int):
    answer = graph[s][a] + graph[s][b]
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer


def solution(n, s, a, b, fares):
    graph = [[math.inf]*(n+1) for _ in range(n + 1)]
    floyd_warshall(graph, n, fares)
    answer = calculate(graph, n, s, a, b)

    return answer


def main():
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


if __name__ == "__main__":
    main()