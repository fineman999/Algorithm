import itertools
from collections import deque

def recursive(answer, check, n, k):
    if n == 0:
        return [answer[0]]
    result = []

    first = k//check[n]
    remain = k%check[n]
    if remain == 0:
        result.append(answer.pop(first-1))
    else:
        result.append(answer.pop(first))
    n -= 1
    k = remain
    return result + recursive(answer, check, n, k)
#
def solution(n, k):
    answer = [i for i in range(1, n+1)]

    check = [0, 1, 2]
    for i in range(3, n):
        check.append(check[i-1]*i)
    # permutations = itertools.permutations(answer, n)
    # cnt = 1
    # for per in permutations:
    #     if cnt == k:
    #         print(per)
    #         break
    #     cnt += 1

    result = recursive(answer, check, n-1, k)
    return result

def main():
    print(solution(20, 788))


if __name__ == "__main__":
    main()