import math

answer = math.inf
def binary_search(n, start, end, times):
    if start > end:
        return
    mid = (start + end) // 2
    members = 0

    total_times = 0
    for timer in times:
        k = mid // timer
        total_times = max(total_times, k * timer)
        members += k

    if members >= n:
        global answer
        answer = min(answer, total_times)
        binary_search(n, start, mid - 1, times)
    elif members < n:
        binary_search(n, mid + 1, end, times)
    else:
        return


def solution(n, times):
    binary_search(n, 0, times[-1] * n, times)
    return answer


def main():
    print(solution(6, [7, 10]))


if __name__ == "__main__":
    main()
