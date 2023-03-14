import heapq
import sys


def solution(N, arr):
    arr.sort()
    heap = []
    # print(arr)
    heapq.heappush(heap, (arr[0][1], arr[0][0]))

    for i in range(1, N):
        [start, end] = arr[i]
        if heap[0][0] <= start:
            (before_end, before_start) = heapq.heappop(heap)
            heapq.heappush(heap, (end, before_start))
        else:
            heapq.heappush(heap, (end, start))
        # print(heap)
    print(len(heap))


def main():
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    solution(N, arr)

if __name__ == '__main__':
    main()