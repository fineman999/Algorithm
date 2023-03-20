import copy
import math
import sys


def solution(N, graph):
    new_graph = copy.deepcopy(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                new_graph[i][j] = min(new_graph[i][k]+new_graph[k][j], new_graph[i][j])

    if new_graph != graph:
        return -1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != k and j != k and graph[i][j] != math.inf and \
                        graph[i][j] == graph[i][k] + graph[k][j]:
                    graph[i][j] = math.inf

    answer = 0
    for i in range(N):
        for j in range(i+1, N):
            if graph[i][j] != math.inf:
                answer += graph[i][j]
    return answer


def main():
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, graph))


if __name__ == '__main__':
    main()
