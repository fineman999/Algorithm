import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0
def dfs(x, y, graph, cycle, cnt, R, C):
    global answer
    # print(cycle)
    answer = max(answer, cnt)

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < R and -1 < nx < C and graph[ny][nx] not in cycle:
            # if graph[ny][nx] in cycle:
            #     global answer
            #     # print(cycle)
            #     answer = max(answer, cnt)
            # else:
            # visited[ny][nx] = True
            cycle.add(graph[ny][nx])
            dfs(nx, ny, graph, cycle, cnt + 1, R, C)
            # visited[ny][nx] = False
            cycle.remove(graph[ny][nx])



def solution(R, C, graph):
    # visited = [[False]*C for _ in range(R)]
    new_graph = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            new_graph[i][j] = ord(graph[i][j])
    # print(new_graph)
    cycle = set()
    cycle.add(new_graph[0][0])
    # visited[0][0] = True


    dfs(0, 0, new_graph, cycle, 1, R, C)

    print(answer)



def main():
    R, C = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(R):
        graph.append(list(sys.stdin.readline().rstrip()))
    solution(R, C, graph)

if __name__ == '__main__':
    main()