from collections import deque, defaultdict
import copy


def bfs(visited, graph, destination, diary):
    q = deque()
    visited[destination] = 0
    q.append((destination, 0))
    while q:
        (before_node, edge) = q.popleft()
        for now_node in graph[before_node]:
            if visited[now_node] == -1:
                q.append((now_node, edge + 1))
                visited[now_node] = edge + 1


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start)
    diary = [-1] * (n + 1)
    result = []
    visited = [-1] * (n + 1)
    bfs(visited, graph, destination, diary)

    for source in sources:
        if source == destination:
            result.append(0)
        else:
            result.append(visited[source])
    return result