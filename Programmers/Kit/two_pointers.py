# n: 데이터의 개수, m: 찾고자 하는 부분합
def solution(n, m, arr):
    cnt = 0
    end = -1
    interval_sum = 0
    for start in range(n):
        while interval_sum < m and end < n:
            end += 1
            interval_sum += arr[end]
        if interval_sum == m:
            cnt += 1
        interval_sum -= arr[start]

    return cnt


def main():
    print(solution(5, 5, [1,2,3,2,5]))


if __name__ == "__main__":
    main()