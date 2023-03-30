import math
import sys
import bisect

def solution(N, arr):
    arr.sort()
    # print(arr)
    answer = [math.inf, 0, 0]
    # k를 pivot이라고 생각하자
    for k in range(N-2):
        # K 다음의 값과, 맨 오른쪽 값을 서로 비교해서 나아가자
        left = k+1
        right = N-1
        # 만약 left > right 가 될 경우 while 문을 빠져 나오자
        while left < right:
            # k + left + right 가 0보자 작을 경우 left를 오른쪽으로 옮기자
            # 아닐 경우 right을 옮기자
            tmp = [arr[k], arr[left], arr[right]]
            sum_tmp = sum(tmp)
            if sum_tmp < 0:
                left += 1
            else:
                right -= 1
            # 그리고 그 결과를 계속 채킹한다.
            if abs(sum_tmp) < abs(sum(answer)):
                answer = tmp

    # answer을 sort하고 끝을 낸다.
    answer.sort()
    return answer



def main():
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = solution(N, arr)
    print(*answer)


if __name__ == '__main__':
    main()