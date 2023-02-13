import heapq
from collections import deque

def solution(jobs):
    answer = []
    jobs.sort()
    jobs = deque(jobs)
    timer = 0
    heap = []
    working = []
    cnt = 0
    # 모두 빈값이 될때 종료
    while jobs or heap or working:
        # 동작중인 디스크가 만료 될 경우
        if working and cnt == working[1]:
            answer.append(timer - working[0])
            working = []

        # 잡에 있는 값이 시간을 만족할 경우
        while jobs and jobs[0][0] == timer:
            [start_time, working_time] = jobs.popleft()
            heapq.heappush(heap, [working_time, start_time])

        # 동작 중인 디스크가 없을 경우 대기 힙에서 동작 시간이 제일 짧은 디스크 가져옴
        if not working:
            if heap and heap[0][1] <= timer:
                [working_time, start_time] = heapq.heappop(heap)
                working = [start_time, working_time]
                cnt = 0

        cnt += 1
        timer += 1

    return sum(answer)//len(answer)


def main():
    print(solution([[0, 3], [1, 9], [2, 6]]))


if __name__ == "__main__":
    main()
