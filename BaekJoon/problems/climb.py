import sys

result = 0
def solution(n):
    dp = [0]*10
    dp[-1] = 1
    for i in range(n+1):
        for k in range(8, -1, -1):
            dp[k] += dp[k+1]
    return dp[0]%10_007
def main():
    n = int(sys.stdin.readline())

    print(solution(n))


if __name__ == "__main__":
    main()