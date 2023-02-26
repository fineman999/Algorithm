import math
import sys

def solution(N):
    answer = [math.inf, math.inf, math.inf, 1, math.inf, 1]
    for i in range(6,N+1):
        answer.append(min(answer[i-3]+1, answer[i-5] + 1))
    if answer[N] == math.inf:
        return -1
    return answer[N]
def main():
    N = int(sys.stdin.readline())
    print(solution(N))

if __name__ == "__main__":
    main()