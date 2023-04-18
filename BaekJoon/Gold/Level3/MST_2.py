import math
import sys
import heapq


def find_parents(direct_visited, node):
    cities = [str(node)]
    while node != direct_visited[node]:
        node = direct_visited[node]
        cities.append(str(node))
    return cities


def input_number():
    return int(sys.stdin.readline().rstrip())


def input_number_with_map():
    return map(int, sys.stdin.readline().rstrip().split())


def dijkstra(visited, graph, heap, direct_visited):

    while heap:
        (weight, node) = heapq.heappop(heap)
        if visited[node] < weight:
            continue
        # print(node)
        for now_node, now_weight in graph[node]:
            new_weight = now_weight + weight

            if visited[now_node] > new_weight:
                direct_visited[now_node] = node
                visited[now_node] = new_weight
                heapq.heappush(heap, (new_weight, now_node))


def solution(n, graph, points):
    heap = []
    [start, end] = points
    visited = [math.inf] * (n + 1)
    direct_visited = {i:i for i in range(n+1)}

    visited[start] = 0

    heapq.heappush(heap, (0, start))

    dijkstra(visited, graph, heap, direct_visited)
    print(visited[end])
    cities = find_parents(direct_visited, end)
    print(len(cities))
    print(" ".join(cities[::-1]))


def main():
    n = input_number()
    m = input_number()
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        start, end, weight = input_number_with_map()
        graph[start].append((end, weight))
    points = list(input_number_with_map())
    solution(n, graph, points)


if __name__ == '__main__':
    main()
