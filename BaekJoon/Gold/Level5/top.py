import sys
from collections import deque

def solution(N, arr):
    answer = [0]*N
    stack = deque()
    for index, value in enumerate(arr):
        if not stack:
            stack.append((index, value))
        else:
            while stack:
                (front_index, front_value) = stack[-1]
                if front_value < value:
                    stack.pop()
                else:
                    answer[index] = front_index + 1
                    break
            stack.append((index, value))
    print(" ".join(list(map(str, answer))))




def main():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, arr)



if __name__ == '__main__':
    main()