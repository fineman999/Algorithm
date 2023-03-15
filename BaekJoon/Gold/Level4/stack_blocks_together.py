import sys


def solution(N, M, H, people):
    dp = [[0]*(H+1) for i in range(N+1)]

    for i in range(N):
        for person in people[i]:
            for k in range(H+1):
                if person == k:
                    dp[i+1][k] += 1
                if dp[i][k] > 0 and k+person < (H+1):
                    dp[i+1][k+person] += dp[i][k]
        for k in range(H+1):
            dp[i+1][k] += dp[i][k]
    #     print(dp)
    # print("answer")
    # print(dp[-1])
    return dp[-1][-1]%10_007


def main():
    N, M, H = map(int, sys.stdin.readline().rstrip().split())
    people = []
    for _ in range(N):
        people.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, M, H, people))

if __name__ == '__main__':
    main()