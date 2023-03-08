import sys
import heapq


def solution(N, arr):
    heap = arr
    heapq.heapify(heap)
    answer = 0
    while heap:
        if len(heap) < 2:

            return answer
        A = heapq.heappop(heap)
        B = heapq.heappop(heap)
        answer += A+B
        heapq.heappush(heap, A+B)

    return answer



def main():
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        arr.append(int(sys.stdin.readline()))
    print(solution(N, arr))


if __name__ == '__main__':
    main()

