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


def direction(queue, game_board, x, y, direct, cnt, depth):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # secret = ["R", "D", "L", "U"]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < ny < len(game_board) and -1 < nx < len(game_board[0]) and game_board[ny][nx] == 0:
            game_board[ny][nx] = cnt
            direct.append([depth, nx, ny])
            queue.append((nx, ny))


def bfs(game_board, q, cnt):
    direct = [[0, q[0][0], q[0][1]]]
    depth = 1
    while q:
        (x, y) = q.popleft()
        direction(q, game_board, x, y, direct, cnt, depth)
        depth += 1
    min_check = [direct[0][1], direct[0][2]]
    # direct.sort(key=lambda x: (x[1], x[2], x[0]))
    direct = [(a, b-min_check[0], c-min_check[1]) for a, b, c in direct]

    # direct.sort()
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
    # print(diary)
    for k in range(4):
        new_table = copy.deepcopy(table)
        # print("start")
        # for ele in table:
        #     print(ele)
        check_cnt = set()
        check_cnt.add(1)
        cnt = 2

        for i in range(len(new_table)):
            for j in range(len(new_table[i])):
                if new_table[i][j] == 0:
                    q.append((j, i))
                    new_table[i][j] = cnt
                    # print("cnt",cnt)
                    check = bfs(new_table, q, cnt)
                    if check in diary:
                        # print("valid")
                        # print(check)
                        diary.remove(check)
                        check_cnt.add(cnt)
                        answer += len(check)
                        break
                    # else:
                    #     print("not valid")
                    #     print(check)
                cnt += 1
        # for ele in new_table:
        #     print(ele)
        table = change_table(new_table, check_cnt)
        # for ele in table:
        #     print(ele)
        table = rotated(table)
    #     print("end")
    # print()
    # print(diary)
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
