from collections import deque, defaultdict
import copy
def rotated(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def direction(queue, game_board, x, y, direct, cnt):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # secret = ["R", "D", "L", "U"]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < ny < len(game_board) and -1 < nx < len(game_board[0]) and game_board[ny][nx] == 0:
            game_board[ny][nx] = cnt
            direct.append((nx, ny))
            queue.append((nx, ny))


def bfs(game_board, q, cnt):
    direct = [(q[0][0], q[0][1])]
    while q:
        (x, y) = q.popleft()
        direction(q, game_board, x, y, direct, cnt)
    direct.sort(key=lambda x:(x[0],x[1]))
    return direct


def change_table(new_table, check_cnt):
    for i in range(len(new_table)):
        for j in range(len(new_table[i])):
            if new_table[i][j] in check_cnt:
                new_table[i][j] = 1
            else:
                new_table[i][j] = 0
    return new_table

def init(game_board, table):
    q = deque()
    diary = []

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                q.append((j, i))
                game_board[i][j] = 1
                direct = bfs(game_board, q, 1)
                diary.append(direct)

    answer = 0

    for k in range(4):
        new_table = copy.deepcopy(table)

        check_cnt = set()
        check_cnt.add(1)
        cnt = 2

        for i in range(len(new_table)):
            for j in range(len(new_table[i])):
                if new_table[i][j] == 0:
                    q.append((j, i))
                    new_table[i][j] = cnt
                    check = bfs(new_table, q, cnt)
                    valid = True
                    # print(check)
                    for element in diary:
                        if len(check) == len(element):
                            # print(element)
                            x_cal = abs(check[0][0] - element[0][0])
                            y_cal = abs(check[0][1] - element[0][1])
                            for h in range(1, len(element)):
                                if abs(element[h][0] - check[h][0]) != x_cal \
                                        or abs(element[h][1] - check[h][1]) != y_cal:
                                    valid = False
                                    break
                            if valid:
                                diary.remove(element)
                                check_cnt.add(cnt)
                                answer += len(check)
                                break
                    cnt += 1

        new_table = change_table(new_table, check_cnt)
        table = rotated(new_table)
    return answer


def solution(game_board, table):
    answer = -1
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1:
                table[i][j] = 0
            else:
                table[i][j] = 1
    answer = init(game_board, table)
    return answer


def main():
    print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))


if __name__ == "__main__":
    main()
