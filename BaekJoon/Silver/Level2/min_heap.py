import sys
import heapq

def solution(N, arr):
    heap = []
    answer = []
    for ele in arr:
        if ele == 0:
            if not heap:
                answer.append(0)
            else:
                answer.append(heapq.heappop(heap))
        else:
            heapq.heappush(heap, ele)
    for ele in answer:
        print(ele)

def main():
    N = int(sys.stdin.readline().rstrip())

    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))
    solution(N, arr)


if __name__ == '__main__':
    main()