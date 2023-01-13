from collections import deque


def solution(n, stations, w):
    stations = deque(stations)
    start = 1
    check = 1 + 2*w
    cnt = 0
    while stations:
        end = stations.popleft() - w
        valid = end - start
        if valid%check == 0:
            cnt -= 1
        cnt += (valid//check + 1)
        start = end + 2*w + 1
    if start == n:
        cnt += 1
    elif start < n:
        valid = n - start + 1
        if valid % check == 0:
            cnt -= 1
        cnt += (valid // check + 1)

    return cnt





def main():
    print(solution(11,[4, 11],	1))


if __name__ == "__main__":
    main()