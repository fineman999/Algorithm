from collections import deque
def solution(queue1, queue2):
    sum_queue = sum(queue1)+sum(queue2)
    if sum_queue % 2 == 1:
        return -1
    result_sum = sum_queue//2
    queue2 = deque(queue2)
    queue1 = deque(queue1)
    cnt = 0
    n = len(queue1) + len(queue2)
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    while result_sum != queue1_sum or result_sum != queue2_sum:
        if cnt> n+2:
            return -1
        if queue1_sum > queue2_sum:
            popleft = queue1.popleft()
            queue1_sum -= popleft
            queue2_sum += popleft
            queue2.append(popleft)
        else:
            popleft = queue2.popleft()
            queue1_sum += popleft
            queue2_sum -= popleft
            queue1.append(popleft)
        cnt += 1

    return cnt


def main():

    return print(solution([3, 2, 7, 2], [4, 6, 5, 1]))


if __name__ == "__main__":
    main()
