import sys
from collections import deque


def bfs(N, K):
    q = deque()
    visited = [-1]*100_001
    visited[N] = 0
    q.append((N, 0))
    while q:
        (now, cnt) = q.popleft()
        # print(now * 2)
        if now == K:
            return cnt
        if 100_001 > now-1 > -1 and visited[now-1] == -1 and visited[now-1] < cnt + 1:
            visited[now-1] = cnt + 1
            q.append((now-1, cnt + 1))
        if 100_001 > now + 1 > -1 and visited[now + 1] == -1 and visited[now + 1] < cnt + 1:
            visited[now + 1] = cnt + 1
            q.append((now + 1, cnt + 1))
        if 100_001 > now*2 > -1 == visited[now * 2] and visited[now * 2] < cnt + 1:
            visited[now*2] = cnt + 1
            q.append((now*2, cnt + 1))
    return 0


def solution(N, K):
    if N == K:
        return 0
    return bfs(N, K)


def main():
    N, K = map(int,sys.stdin.readline().split())
    print(solution(N, K))


if __name__ == "__main__":
    main()