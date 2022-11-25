from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def startDirection(i, j):
    q = deque()
    count = 1
    graph[i][j] = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < len(graph) and 0 <= ny < len(graph):
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                count += 1
                graph[nx][ny] = 0
    return q, count


def direction(q, i, j):
    count = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < len(graph) and 0 <= ny < len(graph):
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                count += 1
                graph[nx][ny] = 0
    return q, count


def BFS(i, j):
    q, count = startDirection(i, j)

    while q:
        x, y = q.popleft()
        q_state, count_state = direction(q, x, y)
        q = q_state
        count += count_state
    return count


def cadastralSurvey(pMap):
    '''
    디지털월드의 국토의 모양이 주어졌을 때, 섬의 갯수 (int) 와 각 섬의 크기들 (list)을 반환하세요.
    '''
    N = len(pMap)
    result = 0
    count_result = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                count_result.append(BFS(i, j))
                result += 1
    count_result.sort()
    return (result, count_result)


def main():
    N = int(input())
    global graph
    graph = [0 for _ in range(N)]
    graph = [list(map(int, input())) for _ in range(N)]
    print(cadastralSurvey(graph))


if __name__ == "__main__":
    main()
