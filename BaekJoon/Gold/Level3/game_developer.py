import copy
import sys
import heapq


def solution(dp, visited, graph, N):
    q = []
    for i in range(N + 1):
        if visited[i] == 0:
            heapq.heappush(q, (dp[i], i))

    while q:
        weight, node = heapq.heappop(q)
        for new_node in graph[node]:
            visited[new_node] -= 1

            if visited[new_node] == 0:
                dp[new_node] += weight
                heapq.heappush(q, (dp[new_node], new_node))

    for i in range(1, N + 1):
        print(dp[i])


def main():
    N = int(sys.stdin.readline().rstrip())
    dp = [0] * (N + 1)
    visited = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        dp[i + 1] = tmp[0]
        for j in range(1, len(tmp) - 1):
            graph[tmp[j]].append(i + 1)
            visited[i + 1] += 1
    solution(dp, visited, graph, N)


if __name__ == '__main__':
    main()
