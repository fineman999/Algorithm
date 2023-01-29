from collections import deque
visited = []

def bfs(graph, queue):

    global visited
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if visited[node] == -1:
                queue.append(node)
                visited[node] = visited[now] + 1


def solution(n, edge):

    global visited
    # print(edge)
    visited = [-1]*(n+1)
    graph = [[] for _ in range(n+1)]
    for ele in edge:
        [node_1, node_2] = ele
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    queue = deque()
    queue.append(1)
    visited[1] = 1
    bfs(graph, queue)
    max_visited = max(visited)
    # print(visited)
    return visited.count(max_visited)


def main():
    print(solution(7,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2],[5,7],[3,7]]))


if __name__ == "__main__":
    main()