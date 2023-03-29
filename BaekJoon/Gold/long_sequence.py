import math
import sys
import bisect

def solution(N, sequence):
    answer = [sequence[0]]
    # dp = [[math.inf] for _ in range(N)]
    # print(dp)
    length = 1
    for i in range(1, N):
        if answer[-1] < sequence[i]:
            answer.append(sequence[i])
            length += 1
        else:
            answer[bisect.bisect_left(answer, sequence[i])] = sequence[i]
    print(length)


def main():
    N = int(sys.stdin.readline().rstrip())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, sequence)

if __name__ == '__main__':
    main()