import copy
import math
from collections import deque


def bfs(graph, visited, start, n):
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        popleft = q.popleft()
        for i in graph[popleft]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    cnt = visited[1:].count(True)
    second_cnt = n - cnt
    return abs(cnt - second_cnt)


def solution(n, wires):
    answer = math.inf

    for i in range(len(wires)):
        new_wires = copy.deepcopy(wires)
        new_wires.pop(i)
        graph = [[] for _ in range(n + 1)]
        for start, end in new_wires:
            graph[start].append(end)
            graph[end].append(start)
        start = 0
        for k in range(len(graph)):
            if graph[k]:
                start = k
                break

        visited = [False]*(n+1)
        answer = min(bfs(graph, visited, start, n), answer)

    return answer

def main():
    print(solution(	9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))


if __name__ == "__main__":
    main()
