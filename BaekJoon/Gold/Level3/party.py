import math
import sys
import heapq


def dijkstra(graph, N, start):
    heap = []
    visited = [math.inf]*(N+1)
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    while heap:
        (weight, node) = heapq.heappop(heap)
        if visited[node] < weight:
            continue
        for now_weight, now_node in graph[node]:
            new_weight = now_weight + weight
            if visited[now_node] > new_weight:
                visited[now_node] = new_weight
                heapq.heappush(heap, (new_weight, now_node))
    return visited


def solution(N, M, X, graph):

    visited = dijkstra(graph, N, X)
    for i in range(1, N+1):
        if i == X:
            continue
        check_visited = dijkstra(graph, N, i)
        visited[i] += check_visited[X]
    answer = 0
    for i in range(1, N+1):
        if visited[i] != math.inf:
            answer = max(answer, visited[i])
    print(answer)


def main():
    N, M, X = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        start, end, weight = map(int, sys.stdin.readline().rstrip().split())
        graph[start].append((weight, end))
    solution(N, M, X, graph)


if __name__ == '__main__':
    main()