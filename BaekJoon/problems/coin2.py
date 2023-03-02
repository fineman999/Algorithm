import math
import sys

result = 0


def solution(n, k, coins):
    # coins = set(coins)
    # coins = list(coins)
    coins.sort()
    # print(coins)
    dp = [math.inf]*(k+1)
    dp[0] = 1
    for j in range(n):
        for i in range(coins[j], k+1):
            if i%coins[j] == 0:
                dp[i] = min(dp[i-coins[j]] + 1, i//coins[j], dp[i])
            else:
                dp[i] = min(dp[i-coins[j]] + 1, dp[i])
    if dp[k] == math.inf:
        return -1
    return dp[k]

def main():
    n,k = map(int,sys.stdin.readline().split())
    coins = []
    for _ in range(n):
        coins.append(int(sys.stdin.readline()))
    print(solution(n, k, coins))


if __name__ == "__main__":
    main()