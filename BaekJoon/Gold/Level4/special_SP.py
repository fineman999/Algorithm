import math
import sys
import heapq
from collections import defaultdict


def dijkstra(start, N, graph, vertex, diary):
    distance = [math.inf] * (N + 1)
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    if start in vertex:
        diary[start] = 0

    while heap:
        (dist, now) = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for node, edge in graph[now]:
            cost = dist + edge
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(heap, (cost, node))
                # print(node, vertex)
                if node in vertex:
                    diary[node] = cost



def solution(N, E, graph, vertex):

    diary = defaultdict(int)
    end_diary = defaultdict(int)
    for ele in vertex:
        diary[ele] = math.inf
        end_diary[ele] = math.inf
    # 1
    dijkstra(1, N, graph, vertex, diary)
    # 2
    mid_diary = defaultdict(int)
    mid_diary[vertex[1]] = math.inf
    dijkstra(vertex[0], N, graph, [vertex[1]], mid_diary)

    dijkstra(N, N, graph, vertex, end_diary)

    first = diary[vertex[0]] + mid_diary[vertex[1]] + end_diary[vertex[1]]
    second = diary[vertex[1]] + mid_diary[vertex[1]] + end_diary[vertex[0]]
    # print(diary)
    # print(mid_diary)
    # print(end_diary)
    if first == math.inf and second == math.inf:
        return -1

    return min(first, second)


def main():
    N, E = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    vertex = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(N, E, graph, vertex))


if __name__ == '__main__':
    main()
