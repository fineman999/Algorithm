import sys
from collections import deque


def direction(q, maps, x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < len(maps) and -1 < ny < len(maps) and maps[ny][nx] == 1:
            q.append((nx, ny))
            cnt += 1
            maps[ny][nx] = 0
    return cnt


def bfs(maps, y, x):
    q = deque()
    q.append((x, y))
    cnt = 1
    maps[y][x] = 0

    while q:
        (x, y) = q.popleft()
        cnt += direction(q, maps, x, y)

    return cnt


def solution(N: int, maps: list):
    cnt = 0
    answer = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                result = bfs(maps, i, j)
                answer.append(result)
                cnt += 1
    answer.sort()

    return (cnt, answer)


def main():
    N = int(sys.stdin.readline())
    maps = []
    for i in range(N):
        maps.append(list(map(int, str(sys.stdin.readline().split()[0]))))

    (cnt, answer) = solution(N, maps)
    print(cnt)
    for element in answer:
        print(element)


if __name__ == "__main__":
    main()