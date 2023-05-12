import sys


def solution(n, files):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    accumulated_sum = [0]
    for i in range(1, n + 1):
        accumulated_sum.append(accumulated_sum[i - 1] + files[i])

    for i in range(2, n + 1):
        for j in range(1, n + 2 - i):
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + \
                               accumulated_sum[j + i - 1] - accumulated_sum[j - 1]

    print(dp[1][n])


def main():
    T = int(sys.stdin.readline())

    for _ in range(T):
        K = int(sys.stdin.readline())
        files = [0] + list(map(int, sys.stdin.readline().split()))
        solution(K, files)



if __name__ == "__main__":
    main()
