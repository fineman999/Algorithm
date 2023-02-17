import sys
import math
def solution(N: int):
    answer = [1,2]
    for i in range(2,N+1):
        answer.append(answer[-1]*2)
    return (answer[N]+1)**2

def main():
    N = int(sys.stdin.readline())
    print(solution(N))


if __name__ == "__main__":
    main()