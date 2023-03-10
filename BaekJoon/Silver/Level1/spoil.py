import math
import sys,bisect


def solution(N, arr):
    plus = []
    minus = []

    for ele in arr:
        if ele > 0:
            plus.append(ele)
        else:
            minus.append(ele)
    if plus:
        plus.sort()
    if minus:
        minus.sort(reverse=True)
    plus_index = 0
    minus_index = 0
    plus_n = len(plus)
    # print(minus)
    minus_n = len(minus)
    # print(minus_n)
    result = []
    answer = [0, math.inf]
    while plus_index < plus_n or minus_index < minus_n:

        if minus_index >= minus_n or (plus_index < plus_n and plus[plus_index] <= abs(minus[minus_index])):
            result.append(plus[plus_index])
            plus_index += 1
        else:
            result.append(minus[minus_index])

            minus_index += 1
        if len(result) == 1:
            continue
        # print(result[-1],result[-2], abs(result[-1] + result[-2]), sum(answer))
        if abs(sum(answer)) > abs(result[-1] + result[-2]):
            answer = [result[-1], result[-2]]

    answer.sort()
    return answer






def main():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = solution(N, arr)
    print(" ".join(list(map(str, answer))))

if __name__ == '__main__':
    main()