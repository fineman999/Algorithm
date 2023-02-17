import sys
import math
def solution(K,P,N):
    answer = [K]
    for i in range(1, N+1):
        answer.append((answer[-1]*P)%1_000_000_007)
    return answer[N]

def main():
    K, P, N = map(int, sys.stdin.readline().split())
    print(solution(K,P,N))

if __name__ == "__main__":
    main()