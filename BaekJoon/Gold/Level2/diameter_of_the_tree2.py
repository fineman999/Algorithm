import math
import sys
import heapq
def dijkstra(N, graph, start):
    visited = [math.inf]*(N+1)
    heap = []
    visited[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        (weight, node) = heapq.heappop(heap)
        for now_weight, now_node in graph[node]:
            if visited[now_node] > now_weight + weight:
                visited[now_node] = now_weight + weight
                heapq.heappush(heap, (visited[now_node], now_node))
    answer = (0, 0)
    # print(visited)
    for i in range(N+1):
        if visited[i] != math.inf:
            if answer[0] < visited[i]:
                answer = (visited[i], i)
    return answer


def solution(N, graph):
    for i in range(len(graph)):
        if graph[i]:
            check = dijkstra(N, graph, i)
            # print(check)
            answer = dijkstra(N, graph, check[1])
            return answer[0]

def main():
    N = int(sys.stdin.readline())
    graph = [[] for _ in range(N+1)]

    for _ in range(N):
        check = list(map(int,sys.stdin.readline().rstrip().split()))
        first = check[0]
        for i in range(1, len(check)-1, 2):
            node, weight = check[i], check[i+1]
            graph[first].append((weight, node))
    print(solution(N, graph))

if __name__ == '__main__':
    main()

