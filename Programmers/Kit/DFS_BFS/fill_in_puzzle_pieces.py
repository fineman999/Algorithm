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


def direction(queue, game_board, x, y, direct):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    secret = ["R", "D", "L", "U"]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < ny < len(game_board) and -1 < nx < len(game_board[0]) and game_board[ny][nx] == 0:
            game_board[ny][nx] = 1
            direct.append(secret[i])
            queue.append((nx, ny))

def table_direction(queue, game_board, x, y, direct, cnt):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    secret = ["R", "D", "L", "U"]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < ny < len(game_board) and -1 < nx < len(game_board[0]) and game_board[ny][nx] == 0:
            game_board[ny][nx] = cnt
            direct.append(secret[i])
            queue.append((nx, ny))

def table_bfs(game_board, q, cnt):
    direct = ['S']
    while q:
        (x, y) = q.popleft()
        table_direction(q, game_board, x, y, direct, cnt)
    return direct

def bfs(game_board, q):
    direct = ['S']
    while q:
        (x, y) = q.popleft()
        direction(q, game_board, x, y, direct)
    return direct


def change_table(new_table, check_cnt):
    for i in range(len(new_table)):
        for j in range(len(new_table[i])):
            if new_table[i][j] == 1 or new_table[i][j] in check_cnt:
                new_table[i][j] = 1
            else:
                new_table[i][j] = 0
    return new_table

def init(game_board, table):
    q = deque()
    diary = defaultdict(int)
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                q.append((j, i))
                game_board[i][j] = 1
                direct = bfs(game_board, q)
                diary["".join(direct)] += 1
    # print(diary)
    answer = 0

    for k in range(4):

        new_table = copy.deepcopy(table)
        check_cnt = set()
        cnt = 2
        # for i in range(len(new_table)):
        #     kkk = []
        #     for j in range(len(new_table[i])):
        #         kkk.append(new_table[i][j])
        #     print(kkk)
        # print()
        for i in range(len(new_table)):
            for j in range(len(new_table[i])):
                if new_table[i][j] == 0:
                    q.append((j, i))
                    new_table[i][j] = cnt
                    compare = table_bfs(new_table, q, cnt)
                    check = "".join(compare)
                    if check in diary:
                        check_cnt.add(cnt)
                        diary[check] -= 1
                        answer += len(check)
                        if diary[check] == 0:
                            del diary[check]
                    cnt += 1
        # print(check_cnt)
        # for i in range(len(new_table)):
        #     kkk = []
        #     for j in range(len(new_table[i])):
        #         kkk.append(new_table[i][j])
        #     print(kkk)
        # print()

        new_table = change_table(new_table, check_cnt)
        # for i in range(len(new_table)):
        #     kkk = []
        #     for j in range(len(new_table[i])):
        #         kkk.append(new_table[i][j])
        #     print(kkk)
        # print()
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
    print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0]],
                   [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                    [0, 1, 0, 0, 0, 0]]))


if __name__ == "__main__":
    main()
