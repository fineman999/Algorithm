import math
import sys

sys.setrecursionlimit(10**6)
visited = []

def recursive(graph, root):

    for node in graph[root]:
        if visited[node] == math.inf:
            visited[node] = root
            recursive(graph, node)



def solution(graph, N):
    global visited
    visited = [math.inf]*(N+1)
    recursive(graph, 1)
    for i in range(2, N+1):
        print(visited[i])

def main():
    N = int(sys.stdin.readline().rstrip())

    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    solution(graph, N)


if __name__ == '__main__':
    main()
