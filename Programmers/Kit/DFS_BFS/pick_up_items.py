import math
from collections import deque

def init_rectangle(graph, rectangle):
    for left_down_x, left_down_y, right_up_x, right_up_y in rectangle:
        for i in range(left_down_x, right_up_x + 1):
            graph[left_down_y][i] = 1
            graph[right_up_y][i] = 1
        for i in range(left_down_y, right_up_y + 1):
            graph[i][right_up_x] = 1
            graph[i][left_down_x] = 1

def check_in_rectangle(rectangle: list, x, y):
    # 하나라도 안에 들어갈 경우
    if any (left_down_x < x < right_up_x and left_down_y < y < right_up_y
            for left_down_x, left_down_y, right_up_x, right_up_y in rectangle):
        return False
    # 이용 가능
    return True

def check_rain_side(rectangle: list, before_x, before_y, after_x, after_y):

    if before_y == after_y:
        if before_x > after_x:
            before_x, after_x = after_x, before_x
        # 하나라도 안에 들어갈 경우
        if any (left_down_x <= before_x < after_x <= right_up_x and
                (before_y == left_down_y or before_y == right_up_y)
                for left_down_x, left_down_y, right_up_x, right_up_y in rectangle):
            return True
    if before_x == after_x:
        if before_y > after_y:
            before_y, after_y = after_y, before_y

        # 하나라도 안에 들어갈 경우
        if any(left_down_y <= before_y < after_y <= right_up_y and
               (before_x == left_down_x or before_x == right_up_x)
                for left_down_x, left_down_y, right_up_x, right_up_y in rectangle):
            return True
    # 이용 가능
    return False

def check_rain_side_final(rectangle: list, before_x, before_y, after_x, after_y):
    if before_y == after_y:
        if before_x > after_x:
            before_x, after_x = after_x, before_x
        # 하나라도 안에 들어갈 경우
        if any (left_down_y < before_y < right_up_y and before_x == left_down_x and
                after_x == right_up_x
                for left_down_x, left_down_y, right_up_x, right_up_y in rectangle):
            return False
    if before_x == after_x:
        if before_y > after_y:
            before_y, after_y = after_y, before_y
        # 하나라도 안에 들어갈 경우
        if any(left_down_x < before_x < right_up_x  and before_y == left_down_y and
                after_y == right_up_y
                for left_down_x, left_down_y, right_up_x, right_up_y in rectangle):
            return False
    # 이용 가능
    return True

def direction(graph, x, y, q: deque, rectangle):
    nx = [0, 1, 0, -1]
    ny = [1, 0, -1, 0]
    for i in range(4):
        dx = nx[i] + x
        dy = ny[i] + y
        if -1 < dx < 102 and -1 < dy < 102 and graph[dy][dx] == 1 \
                and check_in_rectangle(rectangle, dx, dy)\
                and check_rain_side(rectangle, x, y, dx, dy)\
                and check_rain_side_final(rectangle, x, y, dx, dy):
            graph[dy][dx] = graph[y][x] + 1
            q.append((dx, dy))


def bfs(graph, rectangle, q, itemX, itemY):

    while q:
        (x,y) = q.popleft()
        if x == itemX and y == itemY:
            return graph[y][x]
        direction(graph, x, y, q, rectangle)
    return -1


def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0]*102 for _ in range(102)]

    init_rectangle(graph, rectangle)
    q = deque()
    graph[characterY][characterX] = 0
    q.append((characterX, characterY))

    answer = bfs(graph, rectangle, q, itemX, itemY)
    # for i in range(10):
    #     check = []
    #     for j in range(10):
    #         check.append(graph[i][j])
    #     print(check)
    # # print(graph[itemY][itemX])
    return answer


def main():
    print(solution(	[[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))


if __name__ == "__main__":
    main()

