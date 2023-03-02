import sys

result = 0


def solution(n, k, coins):
    coins.sort()
    dp = [0]*(k+1)
    dp[0] = 1
    for j in range(n):
        for i in range(coins[j], k+1):
            dp[i] += dp[i - coins[j]]
    return dp[k]

def main():
    n,k = map(int,sys.stdin.readline().split())
    coins = []
    for _ in range(n):
        coins.append(int(sys.stdin.readline()))
    print(solution(n, k, coins))


if __name__ == "__main__":
    main()