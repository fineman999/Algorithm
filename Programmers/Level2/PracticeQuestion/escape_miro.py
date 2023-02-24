from collections import deque
import copy


def direction(x, y, maps, q, end):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    find_end = False
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < len(maps) and -1 < nx < len(maps[ny]):
            if maps[ny][nx] == 'O':
                q.append((nx, ny))
                # visited[ny][nx] = True
                maps[ny][nx] = maps[y][x] + 1
                # cnt += 1
            elif maps[ny][nx] == end:
                # cnt += 1
                maps[ny][nx] = maps[y][x] + 1
                cnt = maps[ny][nx]
                find_end = True
                break
    return (cnt, find_end)


def bfs(maps, start, end):
    q = deque()
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == start:
                q.append((j, i))
                maps[i][j] = 0
                break
    result_cnt = 0
    next_find = False
    while q:
        (x, y) = q.popleft()
        (result_cnt, find_end) = direction(x, y, maps, q, end)
        if find_end:
            next_find = True
            break
    # print(maps)
    return (result_cnt, next_find)


def solution(maps):
    answer = 0
    new_maps = []
    for i in maps:
        new_maps.append(list(i))
    first_maps = copy.deepcopy(new_maps)
    (result_cnt, next_find) = bfs(first_maps, 'S', 'L')
    if not next_find:
        return -1
    answer += result_cnt
    second_maps = copy.deepcopy(new_maps)
    (result_cnt, next_find) = bfs(second_maps, 'L', 'E')
    if not next_find:
        return -1
    answer += result_cnt
    return answer

