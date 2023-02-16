from collections import deque
import copy
def rotated(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def direction(queue, graph, x, y, direct, cnt):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and graph[ny][nx] == 0:
            graph[ny][nx] = cnt
            direct.append([nx, ny])
            queue.append((nx, ny))


def bfs(graph, q, cnt):
    direct = [[q[0][0], q[0][1]]]
    while q:
        (x, y) = q.popleft()
        direction(q, graph, x, y, direct, cnt)
    # 시작을 0,0으로 고정 하기
    direct = [(b-direct[0][0], c-direct[0][1]) for b, c in direct]
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
                    if check in diary:
                        diary.remove(check)
                        check_cnt.add(cnt)
                        answer += len(check)
                cnt += 1
        table = change_table(new_table, check_cnt)
        table = rotated(table)
    return answer


def solution(game_board, table):
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
