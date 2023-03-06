import sys
from collections import deque
import heapq
def solution(N, M, arr):
    visited = [0]*(N+1)
    graph = [[] for i in range(N+1)]
    for a, b in arr:
        graph[a].append(b)
        visited[b] += 1
    q = []
    for i in range(N, 0, -1):
        if visited[i] == 0:
            heapq.heappush(q, i)
    answer = []
    while q:
        target = heapq.heappop(q)
        answer.append(str(target))
        for i in range(len(graph[target])-1, -1, -1):
            v = graph[target][i]
            visited[v] -= 1
            if visited[v] == 0:
                heapq.heappush(q, v)
    return " ".join(answer)

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(M):
        graph.append(list(map(int, sys.stdin.readline().split())))

    print(solution(N, M, graph))

    # print(solution(8,7, [[1, 3], [1, 4], [3, 5], [5, 4], [5, 6], [3, 7], [2, 8]]))

if __name__ == "__main__":
    main()