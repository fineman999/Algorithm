import math
import sys
import heapq


def dijkstra(graph, start, N):
    visited = [math.inf]*(N+1)
    heap = []
    heapq.heappush(heap, (0, start))
    visited[start] = 0

    while heap:
        (now_weight, now) = heapq.heappop(heap)
        for node, weight in graph[now]:
            if visited[node] > now_weight + weight:
                next_weight = now_weight + weight
                visited[node] = next_weight
                heapq.heappush(heap, (next_weight, node))
    answer = (0, 0)
    # print(visited)
    for i,value in enumerate(visited):
        if value != math.inf:
            if answer[1] < value:
                answer = (i, value)
    return answer

def floyd_warshall(N, arr):
    graph = [[math.inf]*(N+1) for _ in range(N+1)]

    for i in range(N+1):
        graph[i][i] = 0
    for a, b, c in arr:
        graph[a][b] = c
        graph[b][a] = c

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    answer = 0
    for i in range(N+1):
        for j in range(N+1):
            if graph[i][j] != math.inf:
                answer = max(answer, graph[i][j])
    return answer

result = 0

def search_binary(root, node, graph):
    global result
    if not node:
        return 0
    get_direct = 0
    sub_result = 0
    for ele in graph[root]:
        [now_node, now_weight] = ele
        get_child = search_binary(now_node, graph[now_node], graph) + now_weight
        sub_result += get_child
        get_direct = max(get_child, get_direct)

    result = max(sub_result, result)
    return get_direct


def solution(N, arr):

    # print(floyd_warshall(N,arr))

    graph = [[] for _ in range(N + 1)]
    for start, end, weight in arr:
        graph[start].append([end, weight])
        graph[end].append([start, weight])
    answer = 0
    (index, value) = dijkstra(graph,1,N)
    (answer_index, answer_value) = dijkstra(graph, index, N)
    print(answer_value)

    # print(graph)
    # for i in range(1, N+1):
    #     answer = max(answer,dijkstra(graph, i, N))
    # print(answer)
    # left = graph[1][0]
    # right = graph[1][1]
    # print(graph)
    # # graph.sort()
    # search_binary(1, graph[1], graph)
    # print(result)

def main():
    N = int(sys.stdin.readline())
    graph = []
    for _ in range(N-1):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, graph)


if __name__ == '__main__':
    main()
