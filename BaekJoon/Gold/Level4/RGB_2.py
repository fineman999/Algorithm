import math
import sys


def solution(N, graph):
    answer = math.inf
    for k in range(3):
        dp = [[0]*3 for _ in range(N+1)]
        for i in range(3):
            dp[1][i] = math.inf
        dp[1][k] = graph[0][k]
        for i in range(1, N):
            dp[i+1][0] = graph[i][0] + min(dp[i][1], dp[i][2])
            dp[i+1][1] = graph[i][1] + min(dp[i][0], dp[i][2])
            dp[i+1][2] = graph[i][2] + min(dp[i][1], dp[i][0])
        if k == 0:
            answer = min(dp[-1][1], dp[-1][2], answer)
        if k == 1:
            answer = min(dp[-1][2], dp[-1][0], answer)
        if k == 2:
            answer = min(dp[-1][1], dp[-1][0], answer)
        # print(dp)
    print(answer)



def main():
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    solution(N, graph)


if __name__ == '__main__':
    main()