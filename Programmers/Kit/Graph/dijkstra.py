import heapq
import math


def dijkstra(start, distance, graph):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        (dist, now) = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, edge in graph[now]:
            cost = dist + edge
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

def get_distance(distance):
    for index, value in enumerate(distance):
        if value == math.inf:
            print(index, "INFINITY")
        else:
            print(index, value)


# n: 노드의 개수, m: 간선의 개수
def solution(n, m, arr):
    graph = [[] for _ in range(n+1)]
    distance = [math.inf] * (n + 1)
    for start, end, edges in arr:
        graph[start].append((end, edges))

    dijkstra(1, distance, graph)
    get_distance(distance)



def main():
    # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
    print(solution(6,11,[[1,2,2], [1,3,5],[1,4,1],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],
                   [5,3,1],[5,6,2]]))


if __name__ == "__main__":
    main()