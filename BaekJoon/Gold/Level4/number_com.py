import sys
import heapq

def solution(N, arr):
    minus_heap = []
    plus_heap = []
    for ele in arr:
        if ele >0:
            heapq.heappush(plus_heap, -ele)
        else:
            heapq.heappush(minus_heap, ele)

    answer = 0
    while plus_heap:
        if len(plus_heap)>1:
            A = -heapq.heappop(plus_heap)
            B = -heapq.heappop(plus_heap)
            # print(A, B)
            if A+B < A*B:
                answer += A*B
            else:
                answer += A
                heapq.heappush(plus_heap, -B)
        else:
            answer += -heapq.heappop(plus_heap)
    # print(answer)
    while minus_heap:
        if len(minus_heap)>1:
            A = heapq.heappop(minus_heap)
            B = heapq.heappop(minus_heap)
            # print(A, B)
            if A+B < A*B:
                answer += A*B
            else:
                answer += A
                heapq.heappush(minus_heap, B)
        else:
            answer += heapq.heappop(minus_heap)

    print(answer)

def main():
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        arr.append(int(sys.stdin.readline()))
    solution(N, arr)

if __name__ == '__main__':
    main()