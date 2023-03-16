import copy
import sys
from collections import deque, defaultdict


def solution(N, d, k, c, arr):
    dishes = arr + arr[:k]
    eat = defaultdict(int)
    answer = 0
    for i in range(k):
        eat[dishes[i]] += 1
    eat[c] += 1

    left = 0
    for right in range(k, len(dishes)):
        answer = max(answer, len(eat))

        eat[dishes[left]] -= 1
        if eat[dishes[left]] == 0:
            del eat[dishes[left]]
        eat[dishes[right]] += 1
        left += 1
    return answer


def main():
    N, d, k, c = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline()))
    print(solution(N, d, k, c, arr))


if __name__ == '__main__':
    main()
