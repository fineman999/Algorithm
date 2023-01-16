from collections import deque


def bfs(graph, visited, queue, cnt):
    if not queue:
        return visited
    popleft = queue.popleft()
    for element in popleft:
        if visited[element] == -1:
            visited[element] = cnt
            queue.append(graph[element])
            visited = bfs(graph, visited, queue, cnt)
    return visited

def bfs_start(graph, visited, queue):
    visited[0] = 0
    cnt = 1
    for i in range(len(graph)):
        if graph[i]:
            queue.append(graph[i])
            visited[i] = cnt
            break
    visited = bfs(graph, visited, queue, cnt)
    return abs(visited.count(1) - visited.count(-1))

def solution(n, wires):
    answer = 101
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        [a,b] = wire
        graph[a].append(b)
        graph[b].append(a)

    for wire in wires:
        [a,b] = wire
        visited = [-1] * (n + 1)
        graph[a].remove(b)
        graph[b].remove(a)
        queue = deque()
        check = bfs_start(graph, visited,queue)
        answer = min(check, answer)
        graph[a].append(b)
        graph[b].append(a)

    return answer

def main():
    return print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))


if __name__ == "__main__":
    main()
