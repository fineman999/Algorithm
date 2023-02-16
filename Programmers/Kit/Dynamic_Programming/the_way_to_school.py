def solution(m, n, puddles):
    graph = [[0]*m for _ in range(n)]

    for x, y in puddles:
        graph[y-1][x-1] = -1

    for i in range(m):
        if graph[0][i] == -1:
            break
        graph[0][i] = 1
    for i in range(n):
        if graph[i][0] == -1:
            break
        graph[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == -1:
                continue
            if graph[i-1][j] == -1 and graph[i][j-1] == -1:
                continue
            if graph[i-1][j] == -1:
                graph[i][j] = graph[i][j-1]
            elif graph[i][j-1] == -1:
                graph[i][j] = graph[i-1][j]
            else:
                graph[i][j] = (graph[i - 1][j] + graph[i][j-1])%1_000_000_007

    return graph[n-1][m-1]


def main():
    print(solution(	4, 3, [[2, 2]]))


if __name__ == "__main__":
    main()
