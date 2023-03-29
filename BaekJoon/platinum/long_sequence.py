import copy
import sys
import bisect

def solution(N, sequence):
    answer = [sequence[0]]

    dp = [-1]*(N+1)
    dp[0] = 1
    length = 1
    for i in range(1, N):
        if answer[-1] < sequence[i]:
            answer.append(sequence[i])
            length += 1
            dp[i] = length
        else:
            check = bisect.bisect_left(answer, sequence[i])
            dp[i] = check+1
            answer[check] = sequence[i]

    print(length)
    result = []
    for i in range(N - 1, -1, -1):
        if dp[i] == length:
            result.append(sequence[i])
            length -= 1
    result.reverse()
    for r in result:
        print(r, end=' ')




def main():
    N = int(sys.stdin.readline().rstrip())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, sequence)

if __name__ == '__main__':
    main()