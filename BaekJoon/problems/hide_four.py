import sys
from collections import deque

MAX_POINTS = 100_001
def bfs(N, K, visited, diary):
    q = deque()
    q.append(N)

    while q:
        now = q.popleft()
        for node in [now-1, now + 1, now*2]:
            if MAX_POINTS > node > -1 and not visited[node]:
                visited[node] = True
                diary[node] = now
                q.append(node)


def solution(N, K):
    visited = [False]*MAX_POINTS
    visited[N] = True

    diary = [i for i in range(MAX_POINTS)]

    bfs(N, K, visited, diary)
    start = K
    arr = [K]
    cnt = 0
    while diary[start] != start:
        arr.append(diary[start])
        cnt += 1
        start = diary[start]

    return [cnt, " ".join(map(str, arr[::-1]))]


def main():
    N, K = map(int,sys.stdin.readline().split())
    answer = solution(N, K)
    for ele in answer:
        print(ele)


if __name__ == "__main__":
    main()