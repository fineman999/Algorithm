import sys


def solution(n, m, graph):
    # dp = [[0]*m for _ in range(n)]
    # print(graph)
    for i in range(1, n):
        for j in range(1, m):
            check = min(graph[i-1][j-1], graph[i-1][j], graph[i][j-1])
            if check > 0 and graph[i][j] > 0:
                graph[i][j] = max(check + 1, graph[i][j])
    # for ele in graph:
    #     print(ele)
    return max(map(max,graph))

def main():
    n, m = map(int ,sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))

    print(solution(n, m, graph)**2)

if __name__ == '__main__':
    main()