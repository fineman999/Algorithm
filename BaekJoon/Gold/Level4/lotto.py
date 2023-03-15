import sys


def solution(n, m):
    dp = calculate(n, m)
    print(sum(dp[n-1][:m+1]))



def calculate(n, m):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, m+1):
        dp[0][i] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i-1][j] > 0:
                k = j*2
                if k < m+1:
                    dp[i][k] += dp[i-1][j]
        for j in range(1, m+1):
            dp[i][j] += dp[i][j-1]
    # for ele in dp:
    #     print(ele)
    return dp



def main():
    T = int(sys.stdin.readline().rstrip())
    # dp = calculate(4, 10)
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        solution(n, m)

if __name__ == '__main__':
    main()