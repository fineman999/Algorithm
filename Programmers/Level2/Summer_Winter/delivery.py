from collections import deque


def bfs(queue, graph, visited, start, K):
    if not queue:
        return visited

    popleft = queue.popleft()
    for ele in popleft:
        (node, dest) = ele
        if visited[node] == 0 or visited[node] > visited[start] + dest:
            if node == 1 or visited[start] + dest > K:
                continue
            visited[node] = visited[start] + dest
            queue.append(graph[node])
            visited = bfs(queue, graph, visited, node, K)

    return visited


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = dict()
    visited = [0] * (N + 1)
    for ele in road:
        [a, b, dist] = ele
        if a > b:
            a,b = b,a
        if (a, b) not in distance:
            distance[(a, b)] = dist
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        else:
            if dist < distance[(a, b)]:
                distance[(a, b)] = dist
                for i in range(len(graph[a])):
                    if graph[a][i][0] == b:
                        graph[a][i] = (b, dist)
                        break
                for i in range(len(graph[b])):
                    if graph[b][i][0] == a:
                        graph[b][i] = (a, dist)
                        break

    queue = deque()
    queue.append(graph[1])
    visited = bfs(queue, graph, visited, 1, K)
    cnt = 1
    for i in range(1, len(visited)):
        if visited[i] <= K and visited[i] != 0:
            cnt += 1
    return cnt


def main():

    return print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 4], [3, 5, 3], [5, 6, 1]], 4))


if __name__ == "__main__":
    main()
