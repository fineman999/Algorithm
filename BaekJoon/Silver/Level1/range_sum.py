import sys


def solution(N, M, graph, direct):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    dp[1][1] = graph[0][0]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + graph[i - 1][j - 1] - dp[i - 1][j - 1]
    answer = []
    for x1, y1, x2, y2 in direct:
        answer.append(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
    return answer


def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    direct = []
    for i in range(M):
        direct.append(list(map(int, sys.stdin.readline().split())))

    answer = solution(N, M, graph, direct)
    for ele in answer:
        print(ele)


if __name__ == "__main__":
    main()