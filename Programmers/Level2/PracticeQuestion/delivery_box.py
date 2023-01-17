from collections import deque
def solution(order):
    # queue_order = deque(order)
    queue = deque([i for i in range(1,len(order)+1)])
    queue_sub = deque()
    i = 0
    cnt = 0
    for _ in range(len(order)*2):
        if queue:
            popleft = queue.popleft()
            if popleft != order[i]:
                queue_sub.append(popleft)
            else:
                i += 1
        if queue_sub:
            sub_pop = queue_sub.pop()
            if sub_pop == order[i]:
                i += 1
            else:
                queue_sub.append(sub_pop)
    return i


def main():

    return print(solution([5, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
