import math
from collections import Counter, deque


def floyd_warshall(n, computers):
    for computer in computers:
        for j in range(len(computer)):
            if computer[j] == 0:
                computer[j] = math.inf
    for i in range(n):
        computers[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                computers[i][j] = min(computers[i][k]+computers[k][j], computers[i][j])


parents = []

def find_parents(x):
    while x != parents[x]:
        x = parents[x]
    return x


def calculate_union(n, computers):
    global parents
    parents = [i for i in range(n)]
    graph = set()
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph.add((i, j))
    for start, end in graph:
        if find_parents(start) < find_parents(end):
            parents[find_parents(end)] = find_parents(start)
        elif find_parents(start) > find_parents(end):
            parents[find_parents(start)] = find_parents(end)


def bfs(queue, graph, visited):
    while queue:
        popleft = queue.popleft()
        for node in graph[popleft]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


def solution(n, computers):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)

    answer = 0
    visited = [False]*n
    for i in range(len(graph)):
        if not visited[i]:
            visited[i] = True
            queue = deque()
            queue.append(i)
            bfs(queue, graph, visited)
            answer += 1
    return answer

def main():
    print(solution(	3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


if __name__ == "__main__":
    main()
