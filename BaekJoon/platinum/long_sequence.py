import copy
import sys
import bisect

def solution(N, sequence):
    answer = [sequence[0]]
    dp = [1]*(N+1)
    # print(dp)
    # length = 1
    # for i in range(1, N):
    #     if answer[-1] < sequence[i]:
    #         answer.append(sequence[i])
    #         length += 1
    #     else:
    #         answer[bisect.bisect_left(answer, sequence[i])] = sequence[i]
    # print(answer)
    for i in range(len(sequence)):
        for j in range(i):
            if sequence[j] < sequence[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
    # print(dp)
    x = max(dp)

    result = []
    for i in range(N - 1, -1, -1):
        if dp[i] == x:
            result.append(sequence[i])
            x -= 1
    result.reverse()
    for r in result:
        print(r, end=' ')




def main():
    N = int(sys.stdin.readline().rstrip())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, sequence)

if __name__ == '__main__':
    main()