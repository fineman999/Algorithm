import math
import sys
from collections import deque

def solution(N, S, sequence):

    end = 0
    arr_answer = deque()
    sum_answer = 0
    answer = math.inf
    for start in range(N):
        while end < N and sum_answer < S:
            sum_answer += sequence[end]
            arr_answer.append(sequence[end])
            end += 1

        if sum_answer >= S:
            answer = min(len(arr_answer), answer)

        sum_answer -= sequence[start]
        arr_answer.popleft()

    if answer == math.inf:
        return 0
    return answer



def main():
    N, S = map(int, sys.stdin.readline().rstrip().split())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(N, S, sequence))


if __name__ == '__main__':
    main()