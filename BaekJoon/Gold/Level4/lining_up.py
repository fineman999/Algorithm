import sys, bisect

def solution(N, arr):
    dp = [arr[0]]
    for i in range(1, N):
        tmp = bisect.bisect_left(dp, arr[i])
        if len(dp) == tmp:
            dp.append(arr[i])
        else:
            dp[tmp] = arr[i]
    return N - len(dp)


def main():
    N = int(sys.stdin.readline().rstrip())
    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))
    print(solution(N, arr))


if __name__ == '__main__':
    main()