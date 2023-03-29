import math
import sys
import bisect

def solution(N, arr):
    plus = []
    minus = []
    for ele in arr:
        if ele < 0:
            minus.append(ele)
        else:
            plus.append(ele)
    minus.sort(reverse=True)
    answer = []

    plus_index = 0
    minus_index = 0
    plus_n = len(plus)
    minus_n = len(minus)
    result = [0, math.inf]
    cnt = 0

    while plus_index < plus_n or minus_index < minus_n:
        if minus_index >= minus_n or (plus_index < plus_n and plus[plus_index] < abs(minus[minus_index])):
            answer.append(plus[plus_index])
            plus_index += 1
            cnt += 1
        else:
            answer.append(minus[minus_index])
            minus_index += 1
            cnt += 1
        if cnt > 1:
            if abs(sum(result)) > abs(answer[-1] + answer[-2]):
                result = [answer[-1], answer[-2]]

    result.sort()
    return result


def main():
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = solution(N, arr)
    print(answer[0], answer[1])


if __name__ == '__main__':
    main()