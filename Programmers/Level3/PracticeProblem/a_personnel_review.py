import copy
import heapq


def solution(scores):
    answer = 1

    arr = []
    for i in range(len(scores)):
        [a, b] = scores[i]
        arr.append([i, a, b])
    arr.sort(key=lambda x: (-x[1], x[2]))
    # print(arr)
    work = [arr[0]]
    for i in range(1, len(arr)):
        if work[-1][2] <= arr[i][2]:
            work.append(arr[i])

    work.sort(key=lambda x:-(x[1] + x[2]))
    # print(work)
    if work[0][0] == 0:
        return answer
    for i in range(1, len(work)):
        if sum(work[i-1][1:]) != sum(work[i][1:]):
            answer = i + 1
        if work[i][0] == 0:
            return answer

    return -1


def main():
    print(solution(	[[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]]))


if __name__ == '__main__':
    main()
