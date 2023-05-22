import sys
from collections import deque


score = [1, 2, 4, 8]
gears = []

def notValid(left, right):
    if left[2] == right[-2]:
        return True
    return False


def rotate_right(num, direct):
    global gears
    if num + 1 >= 4 or notValid(gears[num], gears[num + 1]):
        return

    rotate_right(num + 1, -direct)
    gears[num+1].rotate(direct)


def rotate_left(num, direct):
    global gears
    if num - 1 <= -1 or notValid(gears[num -1], gears[num]):
        return

    rotate_left(num - 1, -direct)
    gears[num-1].rotate(direct)


def solution(k, sol):
    answer = 0

    for num, direct in sol:
        rotate_right(num-1, -direct)
        rotate_left(num-1, -direct)
        gears[num-1].rotate(direct)
    answer += cal_answer()

    print(answer)

def cal_answer():
    answer = 0
    for i in range(4):
        if gears[i][0] == '1':
            answer += score[i]
    return answer

def main():
    global gears
    for _ in range(4):
        gears.append(deque(list(sys.stdin.readline().rstrip())))
    k = int(sys.stdin.readline())
    sol = []
    for _ in range(k):
        sol.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(k, sol)

if __name__ == '__main__':
    main()