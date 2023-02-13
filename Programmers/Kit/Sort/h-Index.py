import bisect


def solution(citations):
    citations.sort()
    h = citations[-1]
    n = len(citations)

    while h > -1:
        check = bisect.bisect_left(citations, h)
        if n - check >= h >= check - 1:
            return h
        h -= 1


def main():
    print(solution([3, 0, 6, 1, 5]))


if __name__ == "__main__":
    main()
