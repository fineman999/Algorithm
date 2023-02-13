from collections import deque

def solution(progresses, speeds):
    queue = deque()
    for i in range(len(progresses)):
        cnt = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            cnt += 1
        queue.append(cnt)
    check = queue.popleft()
    cnt = 1
    answer = []
    while queue:
        # print(queue)
        compare = queue.popleft()
        if check < compare:
            check = compare
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    # print(cnt)
    if cnt > 0:
        answer.append(cnt)
    return answer

def main():
    print(solution([93, 30, 55],	[1, 30, 5]))

if __name__ == "__main__":
    main()
