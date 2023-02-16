answer = 0
def binary_search(rocks, start, end, n):

    if start > end:
        return
    mid = (end + start) // 2

    check_rocks = 0
    check_distance = 0
    dist = []
    for i in range(1, len(rocks)):
        check_distance += rocks[i] - rocks[i - 1]
        if check_distance >= mid:
            dist.append(check_distance)
            check_distance = 0
        else:
            check_rocks += 1
        if check_rocks > n:
            break
    if check_distance > 0:
        dist.append(check_distance)

    if check_rocks > n:
        binary_search(rocks, start, mid - 1, n)
    else:
        global answer
        result = min(dist)
        answer = max(answer, result)
        binary_search(rocks, mid + 1, end, n)


def solution(distance, rocks, n):
    rocks.sort()
    rocks.insert(0, 0)
    rocks.append(distance)

    end = distance
    binary_search(rocks, 0, end, n)
    return answer

def main():
    print(solution(	25, [2, 14, 11, 21, 17], 2))


if __name__ == "__main__":
    main()
