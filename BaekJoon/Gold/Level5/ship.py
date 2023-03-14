import sys
import heapq
from collections import deque
def solution(N, M, crane, boxes):
    crane.sort(reverse=True)
    boxes.sort(reverse=True)
    # print(crane)
    # print(boxes)

    answer = 0
    heap = deque(boxes)
    if crane[0] < heap[0]:
        return -1
    index = 0
    tmp = deque()
    while heap:
        while heap:
            check = heap.popleft()
            if check <= crane[index]:
                index += 1
            else:
                tmp.append(check)
            if index == N:
                break
        answer += 1
        while tmp:
            heap.appendleft(tmp.pop())
        index = 0

    return answer

def main():
    N = int(sys.stdin.readline())
    crane = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline())
    boxes = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(N, M, crane, boxes))

if __name__ == '__main__':
    main()