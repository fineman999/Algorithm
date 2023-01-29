from collections import deque
def solution(s):
    s = deque(list(s))
    result = 0

    while s:
        x = s.popleft()
        x_cnt = 1
        remain_cnt = 0
        while s:
            remain = s.popleft()
            if x == remain:
                x_cnt += 1
            else:
                remain_cnt += 1
            if remain_cnt == x_cnt:
                break
        if x_cnt > 0 or remain_cnt > 0:
            result += 1
    return result


def main():
    print(solution("abracadabra"))


if __name__ == "__main__":
    main()