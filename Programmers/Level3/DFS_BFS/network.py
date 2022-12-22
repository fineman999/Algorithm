from collections import deque
def bfs(visited, graph, start):
    q = deque(graph[start])
    visited[start] = True
    while q:
        popleft = q.popleft()
        if not visited[popleft]:
           bfs(visited, graph, popleft)


def solution(n, computers):
    visited = [False]*n
    graph = [[] for _ in range(n)]

    for i in range(len(computers)):
        for j in range(i):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    start = 0
    cnt = 0
    while False in visited:
        bfs(visited,graph,start)
        cnt += 1
        for i in range(len(visited)):
            if not visited[i]:
                start = i
                break

    return cnt


def main():
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


if __name__ == "__main__":
    main()
