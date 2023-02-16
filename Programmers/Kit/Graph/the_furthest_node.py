from collections import deque, Counter


def bfs(graph,visited):
    q = deque()
    q.append((1,1))
    visited[1] = 1
    while q:
        (before_node, cnt) = q.popleft()
        for node in graph[before_node]:
            if not visited[node]:
                visited[node] = cnt + 1
                q.append((node, cnt + 1))
    diary = Counter(visited)
    return diary[max(diary.keys())]


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    answer = bfs(graph,visited)
    return answer

def main():
    print(solution(6, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4]]))


if __name__ == "__main__":
    main()