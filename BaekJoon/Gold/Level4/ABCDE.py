import sys

answer = 0
def dfs(graph, visited, node, cnt):

    if cnt == 4:
        global answer
        answer = cnt
        return

    for now in graph[node]:
        if not visited[now]:
            visited[now] = True
            dfs(graph, visited, now, cnt + 1)
            visited[now] = False


def solution(N, M, arr):
    graph = [[] for _ in range(N)]
    for start, end in arr:
        graph[start].append(end)
        graph[end].append(start)


    for i in range(N):
        if graph[i]:
            visited = [False] * N
            visited[i] = True
            cnt = 0
            dfs(graph, visited, i, cnt)
            if answer == 4:
                return 1
    return 0

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(M):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, M, graph))

if __name__ == '__main__':
    main()