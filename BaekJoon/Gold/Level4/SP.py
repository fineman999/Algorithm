import math
import sys
import heapq


def dijkstra(V, start, graph):
    heap = []
    visited = [math.inf]*(V+1)
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    while heap:
        (weight, node) = heapq.heappop(heap)
        for (now_weight, now_node) in graph[node]:
            new_weight = weight + now_weight
            if visited[now_node] > new_weight:
                visited[now_node] = new_weight
                heapq.heappush(heap, (new_weight, now_node))
    return visited


def solution(V, E, start, graph):

    visited = dijkstra(V, start, graph)
    answer = []
    for i in range(1, V+1):
        if visited[i] == math.inf:
            answer.append('INF')
        else:
            answer.append(visited[i])
    print(*answer)


def main():
    V, E = map(int, sys.stdin.readline().rstrip().split())
    start = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        u, v, w = list(map(int, sys.stdin.readline().rstrip().split()))
        graph[u].append((w, v))
    solution(V, E, start, graph)

if __name__ == '__main__':
    main()