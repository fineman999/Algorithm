import bisect
import sys


def solution(N, sequences):
    LIS = [sequences[0]]
    for i in range(1, N):
        index = bisect.bisect_left(LIS, sequences[i])
        if index == len(LIS):
            LIS.append(sequences[i])
        else:
            LIS[index] = sequences[i]
    print(len(LIS))


def main():
    N = int(sys.stdin.readline().rstrip())
    sequences = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, sequences)


if __name__ == '__main__':
    main()