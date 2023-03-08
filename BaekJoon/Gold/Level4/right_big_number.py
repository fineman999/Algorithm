import sys
from collections import deque

def solution(N, arr):
    dp = [-1]*N
    stack = deque()
    for index, value in enumerate(arr):
        if not stack:
            stack.append((index, value))
        else:
            while stack:
                (front_index, front_value) = stack.pop()
                if front_value < value:
                    dp[front_index] = value
                else:
                    stack.append((front_index, front_value))
                    break
            stack.append((index, value))
    print(" ".join(list(map(str, dp))))



def main():
    N = int(sys.stdin.readline())

    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, arr)


if __name__ == "__main__":
    main()