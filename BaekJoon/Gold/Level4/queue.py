import heapq
import math
import sys


def solution(arr, num):
    heap_max = []
    heap_min = []
    for ele in arr:
        if ele[0] == 'I':
            heapq.heappush(heap_max, -int(ele[1]))
            heapq.heappush(heap_min, int(ele[1]))
        elif ele[0] =='D':
            if int(ele[1]) == 1 and heap_max:
                heapq.heappop(heap_max)
                if not heap_max or heap_min[0] > -heap_max[0]:
                    heap_min = []
                    heap_max = []
            elif heap_min:
                heapq.heappop(heap_min)
                if not heap_min or heap_min[0] > -heap_max[0]:
                    heap_max = []
                    heap_min = []
    # print(heap_max, heap_min)
    left = math.inf
    if heap_min:
        left = heapq.heappop(heap_min)
    right = math.inf
    if heap_max:
        right = -heapq.heappop(heap_max)
    if left == math.inf or right == math.inf:
        return "EMPTY"

    return f'{right} {left}'


def main():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        arr = []
        num = int(sys.stdin.readline().rstrip())
        for i in range(num):
            arr.append(list(sys.stdin.readline().rstrip().split()))
        print(solution(arr, num))


if __name__ == '__main__':
    main()
