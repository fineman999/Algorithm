import math
import sys


def solution(N, k):
    start = 0
    end = k
    answer = math.inf
    while start <= end:
        mid = (start + end) // 2

        tmp = 0
        # 1. N행번 동안 각 i행을 나누어서 구하는 값(mid)보다 작을 경우 다 더해준다.
        for i in range(1, N + 1):
            tmp += min(mid//i, N)
        # 2. 만약 tmp가 k보다 작다면 start를 더해준다.
        if tmp < k:
            start = mid + 1
        elif tmp >= k:
            # tmp가 k보다 크거나 같으면 중복된 값들도 있기 때문에 mid가 우리가 구하는 값일 수 도 있다.
            # 더 정확하게 mid를 더 작은 수로 해서 우리가 구하는 k번째 값에 근접하도록 answer을 업데이트 해준다.
            end = mid - 1
            answer = min(answer, mid)
    return answer


def main():
    N = int(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline().rstrip())
    answer = solution(N, k)
    print(answer)

if __name__ == '__main__':
    main()