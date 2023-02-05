import math

answer = math.inf


def binary_search(times, start, end, n):
    if start > end:
        return
    mid = (start + end) // 2
    total_times = 0
    k = 0
    for i in times:
        members = mid//i
        total_times = max(members*i, total_times)
        k += members

    if k >= n:
        global answer
        answer = min(total_times, answer)
        binary_search(times, start, mid - 1, n)
    else:
        binary_search(times, mid + 1, end, n)


def solution(n, times):
    end = times[-1]*n

    binary_search(times, 0, end, n)

    return answer


def main():
    print(solution(10, [6, 8, 10]))


if __name__ == "__main__":
    main()