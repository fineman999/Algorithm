import math
from collections import defaultdict

answer = 0
def binary_search(rocks, start, end, n):

    if start > end:
        return
    mid = (end + start) // 2

    # print("mid",mid)
    check_rocks = 0
    check_distance = 0
    dist = []
    # print(rocks,"rocks")
    # print("mid",mid)
    for i in range(1, len(rocks)):
        check_distance += rocks[i] - rocks[i - 1]
        if check_distance >= mid:
            dist.append(check_distance)
            check_distance = 0
        else:
            check_rocks += 1
    if check_distance > 0:
        dist.append(check_distance)

    if check_rocks == n:
        global answer
        result = min(dist)
        answer = max(answer, result)
    if check_rocks > n:
        binary_search(rocks, start, mid - 1, n)
    else:
        binary_search(rocks, mid + 1, end, n)

def solution(distance, rocks, n):
    rocks.sort()
    rocks.insert(0, 0)
    rocks.append(distance)
    dist = []
    for i in range(1, len(rocks)):
        dist.append(rocks[i]-rocks[i-1])
    global answer
    answer = min(dist)
    end = distance
    binary_search(rocks, 0, end, n)
    return answer

def main():
    print(solution(	25, [2, 14, 11, 21, 17], 2))


if __name__ == "__main__":
    main()
