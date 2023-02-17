import sys
from collections import defaultdict


def solution(names, rooms):
    diary = defaultdict(list)
    for name in names:
        diary[name] = [0] * 18 + [1]

    for room, start, end in rooms:
        if start == 9:
            start = 0
        else:
            start = (start - 9)*2
        end = (end - 9)*2
        # print(start, end)
        diary[room][start:end + 1] = [1] * (end + 1 - start)

    answer = defaultdict(list)
    for key, value in diary.items():
        start = 0
        cnt = 1
        answer_cnt = []
        # print(value)
        for i in range(start, 19):
            if value[i] == 1:
                if cnt > 1:
                    if start == 0:
                        check_start = 9
                    else:
                        check_start = start//2+9
                    check_i = i//2+9
                    if check_start < 10:
                        answer_cnt.append(f"0{check_start}-{check_i}")
                    else:
                        answer_cnt.append(f"{check_start}-{check_i}")
                start = i
                cnt = 1
            else:
                cnt += 1


        answer[key] = answer_cnt

    return answer


def main():
    N, M = map(int, sys.stdin.readline().split())
    names = [sys.stdin.readline().split()[0] for _ in range(N)]
    rooms = []
    for _ in range(M):
        r, s, t = sys.stdin.readline().split()
        rooms.append([r, int(s), int(t)])

    answer = solution(names, rooms)
    answer = list(answer.items())
    answer.sort()

    for i in range(len(answer)):
        (room, times) = answer[i]
        print(f"Room {room}:")
        if len(times) == 0:
            print("Not available")
        else:
            print(f"{len(times)} available:")
            for value in times:
                print(value)
        if i + 1 < len(answer):
            print("-----")


if __name__ == "__main__":
    main()