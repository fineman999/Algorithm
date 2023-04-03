import heapq
import math
import sys
from collections import defaultdict

def solution(arr, num):
    # 최대힙과 최소힙 초기화
    heap_max = []
    heap_min = []
    # index별로 최대힙과 최소힙에 들어간 숫자를 확인
    diary = defaultdict(int)
    # for문 실행
    for i, ele in enumerate(arr):
        # I일 경우 insert
        if ele[0] == 'I':
            heapq.heappush(heap_max, (-int(ele[1]), i))
            heapq.heappush(heap_min, (int(ele[1]), i))
            diary[i] += 1
        elif ele[0] =='D':
            # D일 경우 1이면 ㅁ
            if int(ele[1]) == 1:
                while heap_max and heap_max[0][1] not in diary:
                    heapq.heappop(heap_max)
                if heap_max:
                    del diary[heapq.heappop(heap_max)[1]]
            else:
                while heap_min and heap_min[0][1] not in diary:
                    heapq.heappop(heap_min)
                if heap_min:
                    del diary[heapq.heappop(heap_min)[1]]

    # 들어가지 않은 값 확인
    while heap_max and heap_max[0][1] not in diary:
        heapq.heappop(heap_max)
    while heap_min and heap_min[0][1] not in diary:
        heapq.heappop(heap_min)

    if not heap_min or not heap_max:
        return "EMPTY"
    return f'{-heap_max[0][0]} {heap_min[0][0]}'


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
