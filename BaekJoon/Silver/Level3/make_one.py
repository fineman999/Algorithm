import math
import sys

def solution(N):
    answer = [math.inf, 0, 1, 1]

    for i in range(4, N+1):
        num_2 = 0
        num_3 = 0
        if i%3 == 0:
            num_3 = i//3
        if i%2 == 0:
            num_2 = i//2
        answer.append(min(answer[i-1], answer[num_3], answer[num_2]) + 1)
    # print(answer)
    return answer[N]
def main():
    N = int(sys.stdin.readline())
    print(solution(N))

if __name__ == "__main__":
    main()