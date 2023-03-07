import sys
import heapq

def solution(N, arr):

    heap_minus = []
    heap_plus = []
    answer = []
    for ele in arr:
        if ele == 0:
            check = 0
            if heap_plus and heap_minus:
                check_plus = heapq.heappop(heap_plus)
                check_minus = -heapq.heappop(heap_minus)

                if abs(check_plus) >= abs(check_minus):
                    check = check_minus
                    heapq.heappush(heap_plus, check_plus)
                else:
                    check = check_plus
                    heapq.heappush(heap_minus, -check_minus)
            elif heap_plus:
                check = heapq.heappop(heap_plus)
            elif heap_minus:
                check = -heapq.heappop(heap_minus)
            answer.append(check)
        else:
            if ele < 0:
                heapq.heappush(heap_minus, abs(ele))
            else:
                heapq.heappush(heap_plus, ele)

    return answer


def main():
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        arr.append(int(sys.stdin.readline()))
    answer = solution(N, arr)
    for ele in answer:
        print(ele)

if __name__ == "__main__":
    main()