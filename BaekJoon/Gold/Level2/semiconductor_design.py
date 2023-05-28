import sys
import bisect

def solution(n, sequence):
    answer = [sequence[0]]
    for i in range(1, n):
        if answer[-1] < sequence[i]:
            answer.append(sequence[i])
        else:
            temp = bisect.bisect_left(answer, sequence[i])
            answer[temp] = sequence[i]

    print(len(answer))




def main():
    n = int(sys.stdin.readline().rstrip())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, sequence)

if __name__ == '__main__':
    main()