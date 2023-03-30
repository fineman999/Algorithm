import math
import sys
from collections import defaultdict
import bisect

def solution(N, M, apps, weights, m):
    apps.sort()

    answer = math.inf
    K = sum(weights)
    dp = [[0]*(K+1) for i in range(N+1)]
    for i in range(N):
        value, weight = apps[i]
        for j in range(K+1):
            if j - weight >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-weight] + value)
            else:
                dp[i+1][j] = dp[i][j]
            if dp[i+1][j] >= M:
                answer = min(answer, j)
                break

        # for ele in dp:
        #     print(ele)

    return answer




def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    m = list(map(int,sys.stdin.readline().rstrip().split()))
    weights = list(map(int,sys.stdin.readline().rstrip().split()))
    apps = []
    for i in range(N):
        apps.append((m[i], weights[i]))

    print(solution(N, M, apps, weights, m))


if __name__ == '__main__':
    main()