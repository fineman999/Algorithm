import heapq
from collections import deque


def get_working(heap, cnt):
    [timer, start] = heap[0]
    working = []
    working_timer = 0
    if cnt >= start:
        working = [start, timer]
        heapq.heappop(heap)
    return working, working_timer


def solution(jobs):
    answer = []
    jobs.sort()
    jobs = deque(jobs)

    working = []
    heap = []
    cnt = 0
    working_timer = 0
    while True:
        if not jobs and not working and not heap:
            break

        # 힙에 넣기
        while jobs:
            [start, timer] = jobs.popleft()
            if cnt >= start:
                heapq.heappush(heap, [timer, start])
            else:
                jobs.appendleft([start, timer])
                break

        # 동작 하지 않을 때
        if not working and heap:
            (working, working_timer) = get_working(heap, cnt)

        # 동작할 경우
        if working:
            [start, timer] = working
            if timer <= working_timer:
                working = []
                answer.append(cnt-start)
                if heap:
                    (working, working_timer) = get_working(heap, cnt)

        working_timer += 1
        cnt += 1

    return sum(answer)//len(answer)


def main():
    print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))


if __name__ == "__main__":
    main()