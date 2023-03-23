import math
import sys

diary = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}


def solution(num):
    dp_max = [0, 0]
    dp_min = [0, 0]
    for i in range(2, num + 1):
        check_max = 0
        check_min = math.inf
        for key, value in diary.items():
            if i - key > 1:
                check_max = max(int(str(dp_max[i - key]) + str(max(value))),
                                int(str(max(value)) + str(dp_max[i - key])),
                                check_max)
                front = str(dp_min[i-key])
                back = str(min(value))
                if len(front) + len(back) == len(str(int(front+back))):
                    check_min = min(check_min, int(front+back))
                elif len(front) + len(back) == len(str(int(back + front))):
                    check_min = min(check_min, int(back + front))
        if i in diary:
            check_max = max(check_max, max(diary[i]))
            check_min = min(check_min, min(diary[i]))
        if check_min == 0:
            check_min = 6
        dp_max.append(check_max)
        dp_min.append(check_min)

    print(dp_min[-1], dp_max[-1])


def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        solution(int(sys.stdin.readline().rstrip()))


if __name__ == '__main__':
    main()
