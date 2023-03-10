import math
import sys



def find_prime(visited, n):
    visited[0] = True
    visited[1] = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if not visited[i]:
            j = 2
            while j*i < n+1:
                visited[j*i] = True
                j += 1



def solution(N):
    visited = [False] * (N+2)
    find_prime(visited, N)
    check = []
    for i, valid in enumerate(visited):
        if not valid:
            check.append(i)

    end = -1
    interval_sum = 0
    length = len(check)
    cnt = 0
    for start in range(length):
        while interval_sum < N and end < length:
            end += 1
            interval_sum += check[end]
        if interval_sum == N:
            cnt += 1
        interval_sum -= check[start]
    return cnt



def main():
    N = int(sys.stdin.readline())
    print(solution(N))

if __name__ == '__main__':
    main()

