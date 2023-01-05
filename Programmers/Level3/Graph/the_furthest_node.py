from collections import deque
visited = []

def bfs(graph, start, queue):

    global visited
    while queue:
        queue_popleft = queue.popleft()
        for ele in queue_popleft:
            if visited[ele] == -1 or visited[ele] > 1 + visited[start]:
                visited[ele] = 1 + visited[start]

        for ele in queue_popleft:
                set_ele = []
                for i in range(len(graph[ele])):
                    if visited[graph[ele][i]] == -1 or visited[graph[ele][i]] > visited[ele] + 1 or graph[ele][i] != start:
                        visited[graph[ele][i]] = visited[ele] + 1
                        set_ele.append(graph[ele][i])
                if set_ele:
                    queue.append(set_ele)
                    bfs(graph, ele, queue)

def solution(n, edge):
    global visited
    visited = [-1]*(n+1)
    graph = [[] for _ in range(n+1)]
    for ele in edge:
        [node_1, node_2] = ele
        # if node_1 > node_2:
        #     node_1, node_2 = node_2, node_1
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)
    print(graph)
    # setting
    queue = deque()
    queue.append(graph[1])
    visited[1] = 0
    bfs(graph, 1, queue)

    max_visited = max(visited)

    return visited.count(max_visited)


def main():
    print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


if __name__ == "__main__":
    main()