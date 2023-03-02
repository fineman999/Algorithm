import sys
from itertools import combinations
from collections import defaultdict


n = 6
W = 21
w = [0, 5, 6,10,11,16]

def promising(i, weight, total):
    if i+1 <= n and weight + total >= W and (weight == W or weight + w[i+1] <= W):
        return True
    return False


def sum_of_subsets(i, weight, total, include):
    print(weight, W, total)
    if promising(i, weight, total):

        if weight == W:
            print(include[1:])
        else:
            include[i + 1] = True
            sum_of_subsets(i + 1, weight + w[i+1], total - w[i+1], include)
            include[i + 1] = False
            sum_of_subsets(i + 1, weight, total - w[i+1], include)


def solution():
    count = 0

    total = sum(w)
    include = [False] * (n+1)
    print(total)
    sum_of_subsets(0, 0, total,include)

    return count


def main():
    # N, S = map(int, sys.stdin.readline().split())
    # seq = list(map(int, sys.stdin.readline().split()))
    # answer = solution(N, S, seq)
    solution()
    # print(answer)


if __name__ == "__main__":
    main()
