import math
import sys
result = []
def dfs(N, M, cnt, seq):
    if M == cnt:
        global result
        result.append(seq)
        return
    for i in range(1,N+1):
        dfs(N, M, cnt + 1, seq + [i])


def solution(N, M):
    dfs(N, M, 0, [])

    return result


def main():
    N, M = map(int, sys.stdin.readline().split())
    answer = solution(N, M)
    for ele in answer:
        print(" ".join(list(map(str, ele))))



if __name__ == "__main__":
    main()