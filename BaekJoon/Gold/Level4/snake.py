import math
import sys
from collections import deque, defaultdict


def bfs(visited, ladders, snakes):
    q = deque()
    q.append((1, 0))
    visited[1] = True
    while q:
        (loc, cnt) = q.popleft()
        if loc == 100:
            return cnt
        for i in range(1, 7):
            now = loc + i
            if 0 < now < 101 and not visited[now]:
                if now in ladders:
                    now = ladders[now]

                if now in snakes:
                    now = snakes[now]
                if not visited[now]:
                    visited[now] = True
                    q.append((now, cnt + 1))
        # print(q)
    return -1


def solution(N, M, ladders, snakes):
    visited = [False] * 101
    answer = bfs(visited, ladders, snakes)
    print(answer)


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    ladders = defaultdict(int)
    for _ in range(N):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        ladders[A] = B
    snakes = defaultdict(int)
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        snakes[A] = B
    solution(N, M, ladders, snakes)


if __name__ == '__main__':
    main()
