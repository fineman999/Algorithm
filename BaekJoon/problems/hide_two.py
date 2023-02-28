import math
import sys
from collections import deque, defaultdict


def bfs(N, K, diary, visited):
    q = deque()
    visited[N] = 0
    q.append(N)
    answer = 0
    while q:
        now = q.popleft()
        diary[now] += 1

        for node in [now-1, now + 1, now * 2]:
            if 100_001 > node > -1 and (visited[node] == -1 or visited[node] >= visited[now] + 1):
                visited[node] = visited[now] + 1
                q.append(node)

    return answer


def solution(N, K):

    diary = defaultdict(int)
    visited = [-1] * 100_001
    bfs(N, K, diary, visited)
    return [visited[K], diary[K]]


def main():
    N, K = map(int, sys.stdin.readline().split())
    answer = solution(N, K)
    for ele in answer:
        print(ele)


if __name__ == "__main__":
    main()
