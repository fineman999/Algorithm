from collections import deque


def direction(q: deque, maps: list, x: int, y: int):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1< ny < len(maps) and -1 < nx< len(maps[ny]) and maps[ny][nx] != "X":
            cnt += int(maps[ny][nx])
            maps[ny][nx] = "X"
            q.append((nx, ny))
    return cnt


def bfs(maps, j, i):
    q = deque()
    q.append((j, i))
    cnt = int(maps[i][j])
    maps[i][j] = "X"

    while q:
        (x, y) = q.popleft()
        cnt += direction(q, maps, x, y)
    return cnt


def solution(maps):
    maps = [list(element) for element in maps]
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != "X":
                answer.append(bfs(maps, j, i))
    if not answer:
        return [-1]
    answer.sort()
    return answer

def main():
    print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))

if __name__ == "__main__":
    main()