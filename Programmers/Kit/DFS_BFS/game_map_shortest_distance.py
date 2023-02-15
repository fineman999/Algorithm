from collections import deque

def direction(queue: deque, maps: list, n, m, x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < ny < n and -1 < nx < m and maps[ny][nx] == 1:
            maps[ny][nx] = maps[y][x] + 1
            queue.append((nx, ny))


def bfs(maps, queue):
    n = len(maps)
    m = len(maps[0])
    while queue:
        (x, y) = queue.popleft()
        direction(queue, maps, n, m, x, y)

def solution(maps):
    queue = deque()
    queue.append((0, 0))
    maps[0][0] = 2
    bfs(maps, queue)
    # print(maps)
    if maps[-1][-1] == 1:
        return -1
    return maps[-1][-1] - 1

def main():
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))


if __name__ == "__main__":
    main()
