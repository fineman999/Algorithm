import math
import sys
import bisect
# def solution(N, arr):
#     dp = [0]*N
#     for i in range(N):
#         dp[i] = 1
#         for j in range(N):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#         print(dp)
#     return dp

def solution(N, arr):
    dp = [arr[0]]
    for i in range(1, N):
        check = bisect.bisect_left(dp, arr[i])
        if check == len(dp):
            dp.append(arr[i])
        else:
            dp[check] = arr[i]
    return len(dp)
def main():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solution(N, arr))

if __name__ == "__main__":
    main()