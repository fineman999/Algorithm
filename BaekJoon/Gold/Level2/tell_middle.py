import sys
import heapq


def solution(arr):
    left = []
    right = []
    left_cnt = 0
    right_cnt = 0

    for num in arr:
        if left_cnt == right_cnt:
            increase_left(left, num, right)
            left_cnt += 1
        else:
            increase_right(left, num, right)
            right_cnt += 1

        print_answer(left, left_cnt, right, right_cnt)


def increase_right(left, num, right):
    if right and right[0] < num:
        heapq.heappush(right, num)
    elif left and -left[0] > num:
        heapq.heappush(right, -heapq.heappop(left))
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)


def increase_left(left, num, right):
    if right and right[0] < num:
        heapq.heappush(left, -heapq.heappop(right))
        heapq.heappush(right, num)
    else:
        heapq.heappush(left, -num)


def print_answer(left, left_cnt, right, right_cnt):
    if left_cnt >= right_cnt:
        print(-left[0])
    else:
        print(right[0])


def main():
    N = int(sys.stdin.readline().rstrip())
    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))
    solution(arr)


if __name__ == '__main__':
    main()
