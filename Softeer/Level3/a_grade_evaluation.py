import sys
import copy
from collections import defaultdict


def solution(N, competition):
    answer = []
    for i in range(4):
        arr = copy.deepcopy(competition[i])
        arr.sort(reverse=True)
        rank = defaultdict(int)
        rank[arr[0]] = 1

        for j in range(1, N):
            if arr[j - 1] == arr[j]:
                continue
            rank[arr[j]] = j + 1
        result = []
        for j in range(N):
            result.append(str(rank[competition[i][j]]))
        answer.append(result)

    return answer


def main():
    N = int(sys.stdin.readline())
    competition = []
    for i in range(3):
        competition.append(list(map(int, sys.stdin.readline().split())))
    arr = copy.deepcopy(competition[0])
    for i in range(1, 3):
        for j in range(N):
            arr[j] += competition[i][j]
    competition.append(arr)
    answer = solution(N, competition)
    for element in answer:
        print(" ".join(element))


if __name__ == "__main__":
    main()