import sys
import heapq


def solution(N, K, times, buildings, W, degrees):
    visited = [0]*(N+1)
    heap = []

    for i in range(1, N+1):
        if degrees[i] == 0:
            heapq.heappush(heap, (0, i))
            visited[i] = times[i-1]

    while heap:
        cnt, node = heapq.heappop(heap)

        for now in buildings[node]:
            visited[now] = max(times[now-1] + visited[node], visited[now])
            degrees[now] -= 1
            if degrees[now] == 0:
                heapq.heappush(heap, (cnt+1, now))

    return visited[W]


def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, K = map(int, sys.stdin.readline().rstrip().split())
        times = list(map(int, sys.stdin.readline().rstrip().split()))
        degrees = [0]*(N+1)
        buildings = [[] for _ in range(N+1)]
        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().rstrip().split())
            buildings[X].append(Y)
            degrees[Y] += 1
        W = int(sys.stdin.readline().rstrip())
        answer = solution(N, K, times, buildings, W, degrees)
        print(answer)


if __name__ == '__main__':
    main()

