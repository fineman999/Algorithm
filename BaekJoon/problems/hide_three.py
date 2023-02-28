import sys
from collections import deque
MAX_POINTS = 100_001


def bfs(visited, N, K):
    q = deque()
    q.append(N)
    visited[N] = 0
    while q:
        now = q.popleft()
        for node in [now-1, now+1]:
            if -1 < node < MAX_POINTS and (visited[node] == -1 or visited[now] + 1 <= visited[node]):
                visited[node] = visited[now] + 1
                q.append(node)
        if -1 < now*2 < MAX_POINTS and (visited[now*2] == -1 or visited[now] < visited[now*2]):
            visited[now*2] = visited[now]
            q.append(now*2)



def solution(N, K):
    visited = [-1]*MAX_POINTS
    bfs(visited, N, K)

    print(visited[K])

def main():
    N, K = map(int, sys.stdin.readline().split())
    solution(N, K)



if __name__ == "__main__":
    main()
