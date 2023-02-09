from collections import deque


def calculate(queue, time_shuttle, m):
    result = 0
    for i in range(len(time_shuttle)):
        cnt = 0
        if i == len(time_shuttle) - 1:
            result = time_shuttle[i]
            check = 0
            while queue:
                if cnt == m - 1:
                    if check != 0:
                        if queue and queue[0] == check:
                            result = check - 1
                        else:
                            result = check
                    else:
                        if queue and time_shuttle[i] >= queue[0]:
                            result = queue[0] - 1
                    break
                if queue[0] <= time_shuttle[i]:
                    check = queue.popleft()
                    cnt += 1
                else:
                    break
            break

        while queue:
            if cnt == m:
                break
            if queue[0] <= time_shuttle[i]:
                queue.popleft()
                cnt += 1
            else:
                break

    hour = "00"+str(result//60)
    minutes = "00"+str(result % 60)
    return f"{hour[-2:]}:{minutes[-2:]}"


def solution(n, t, m, timetable):

    timetable = [int(clock.split(":")[0])*60 + int(clock.split(":")[1]) for clock in timetable]
    timetable.sort()

    queue = deque(timetable)
    time_shuttle = [9*60]
    for i in range(1, n):
        time_shuttle.append(time_shuttle[-1]+t)

    return calculate(queue, time_shuttle, m)



def main():
    print(solution(1, 1, 1, ["09:02"]))


if __name__ == "__main__":
    main()