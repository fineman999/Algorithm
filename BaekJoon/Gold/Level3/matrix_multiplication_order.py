import math
import sys


def solution(N, matrix):
    result = 0

    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        for y in range(N-i):
            x = i + y
            if x == y:
                continue
            dp[y][x] = math.inf
            for k in range(y, x):
                dp[y][x] = min(dp[y][x], dp[y][k] + dp[k+1][x] + matrix[y]*matrix[k+1]*matrix[x+1])

    print(dp[0][-1])


def main():
    N = int(sys.stdin.readline().rstrip())
    matrix = list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(N-1):
        _, num = list(map(int, sys.stdin.readline().rstrip().split()))
        matrix.append(num)
    solution(N, matrix)


if __name__ == '__main__':
    main()