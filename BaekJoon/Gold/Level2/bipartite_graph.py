import math
import sys
sys.setrecursionlimit(10**6)

def dfs(node, graph, cnt, visited):

    for i in graph[node]:
        if visited[i] == math.inf:
            visited[i] = cnt
            dfs(i, graph, -cnt, visited)



def solution(v, e, graph):
    visited = [math.inf] * (v+1)

    for i in range(1, v+1):
        if visited[i] == math.inf:
            visited[i] = 1
            dfs(i, graph, -1, visited)

    for i in range(1, v+1):
        for j in graph[i]:
            if visited[i] == visited[j]:
                return "NO"
    return "YES"







def main():
    k = int(sys.stdin.readline().rstrip())

    for _ in range(k):
        v, e = map(int, sys.stdin.readline().rstrip().split())
        graph = [[] for _ in range(v+1)]
        for _ in range(e):
            left, right = map(int, sys.stdin.readline().rstrip().split())
            graph[left].append(right)
            graph[right].append(left)
        answer = solution(v, e, graph)
        print(answer)


if __name__ == '__main__':
    main()

