from collections import deque
boards = []
cnt = 0
board_set = set()
check_ele = [(1,0),(1,1),(0,1)]
def insert_board_set(x,y):
    board_set.add((x,y))
    for ele in check_ele:
        (dx, dy) = ele
        nx = dx + x
        ny = dy + y
        board_set.add((nx, ny))

def direction(x,y):
    valid = True
    for ele in check_ele:
        (dx, dy) = ele
        nx = dx + x
        ny = dy + y
        if boards[y][x] != boards[ny][nx]:
            valid = False
            break
    if valid:
        insert_board_set(x,y)


def solution(m, n, board):
    global cnt
    global board_set
    # 1. 문자열을 배열에 넣기
    for ele in board:
        boards.append(list(ele))

    while True:
        # 2. boards의 값이 0이 아니고 같은 문자일 씨 boards_set에 넣기
        for i in range(m-1):
            for j in range(n-1):
                if boards[i][j] != "0":
                    direction(j,i)
        # 3. boards_set이 0이면 같은 값이 없으므로 나가기
        if not board_set:
            break
        # 4. 같은 값 모두 0으로 바꾸기와 동시에 해당되는 값 카운트
        while board_set:
            (x, y) = board_set.pop()
            boards[y][x] = "0"
            cnt += 1
        # 5. 큐와 스택을 이용해 y축으로 쌓아서 다시 재정렬하기
        for i in range(n):
            check_queue = deque()
            for j in range(m):
                if boards[j][i] != "0":
                    check_queue.append(boards[j][i])
            if len(check_queue) == m:
                continue
            for j in range(m-1,-1,-1):
                if check_queue:
                    boards[j][i] = check_queue.pop()
                else:
                    boards[j][i] = "0"

    return cnt


def main():
    print(solution(4,	5,	["CCBDE", "AAADE", "AAABF", "CCBBF"]))


if __name__ == "__main__":
    main()
