
import sys
import copy
from collections import deque
import heapq

def bfs(N, M, V, graph):
    visited = [False] * (N + 1)
    visited[V] = True
    q = deque()
    q.append(V)
    answer = [V]
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                answer.append(i)
                visited[i] = True
                q.append(i)
    return answer

result = []
def dfs(N, V, visited, graph):
    global result
    result.append(V)
    visited[V] = True
    for i in graph[V]:
        if not visited[i]:
            dfs(N, i, visited, graph)



def solution(N, M, V, arr):
    graph = [[] for _ in range(N+1)]
    for start, end in arr:
        graph[start].append(end)
        graph[end].append(start)
    for i in range(N):
        graph[i].sort()
    answer = []
    visited = [False]*(N+1)
    dfs(N, V, visited, graph)

    answer.append(result)
    answer.append(bfs(N, M, V, graph))
    for ele in answer:
        print(" ".join(map(str, ele)))

def main():
    N, M, V = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(M):
        graph.append(list(map(int, sys.stdin.readline().split())))
    graph.sort()

    solution(N, M, V, graph)


if __name__ == "__main__":
    main()