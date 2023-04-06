import sys
import bisect


def repeated(tmp, sequence, mid, k):
    if not tmp and sequence[k] < mid:
        tmp.append(sequence[k])
    else:
        if sequence[k] < mid:
            if tmp[-1] < sequence[k]:
                tmp.append(sequence[k])
            else:
                check = bisect.bisect_left(tmp, sequence[k])
                tmp[check] = sequence[k]


def solution(N, sequence):
    answer = 0
    for i in range(N):
        mid = sequence[i]
        tmp = []
        sub_answer = 1
        for k in range(i):
            repeated(tmp, sequence, mid, k)
        sub_answer += len(tmp)

        tmp = []
        for k in range(N - 1, i, -1):
            repeated(tmp, sequence, mid, k)
        sub_answer += len(tmp)

        answer = max(sub_answer, answer)

    print(answer)


def main():
    N = int(sys.stdin.readline().rstrip())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, sequence)


if __name__ == '__main__':
    main()
