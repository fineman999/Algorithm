
import sys



def solution(K, N, graph):
    graph.sort()
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        [weight, value] = graph[i-1]
        # print(weight,value)
        for k in range(1, K+1):

            if k - weight >= 0:
                dp[i][k] = max(dp[i-1][k], dp[i-1][k-weight] + value)
            else:
                dp[i][k] = dp[i - 1][k]
    # print(dp)
    return dp[-1][-1]

def main():
    N, K = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    print(solution(K, N, graph))
if __name__ == "__main__":
    main()