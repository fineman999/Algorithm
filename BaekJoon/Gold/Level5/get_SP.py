import math
import sys
import heapq


def dijkstra(graph, start, N):
    heap = []
    heapq.heappush(heap, (0, start))
    visited = [math.inf] * (N + 1)
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



def solution(graph, start, end, N):

    visited = dijkstra(graph, start, N)

    if visited[end] == math.inf:
        return -1
    return visited[end]
    
    


def main():
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        start, end, weight = map(int, sys.stdin.readline().rstrip().split())
        graph[start].append((weight, end))
        
    start, end = map(int, sys.stdin.readline().rstrip().split())
    answer = solution(graph, start, end, N)
    print(answer)
    
if __name__ == '__main__':
    main()
        