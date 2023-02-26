import math
import sys
def solution(N, steps):
    if N == 1:
        return steps[0]

    answer = [steps[0], steps[1]+steps[0]]
    if N > 2:
        answer.append(max(steps[1] + steps[2], steps[0] + steps[2]))

    for i in range(3,N): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        answer.append(max(answer[i-3]+steps[i-1]+steps[i], answer[i-2]+steps[i]))

    return answer[N-1]

def main():
    N = int(sys.stdin.readline())
    steps = []
    for i in range(N):
        steps.append(int(sys.stdin.readline()))

    print(solution(N, steps))


if __name__ == "__main__":
    main()
