import copy

check = ["O", "X"]
result = 0


def check_valid(visited):
    if all(-1 not in element for element in visited):
        global result
        result = 1
        return True
    return False


def pre_win(visited, cnt, i, j):
    global result
    if all(cnt % 2 == k for k in visited[i]):
        if check_valid(visited):
            result = 1
        return 0
    if cnt % 2 == visited[0][j] and cnt % 2 == visited[1][j] and cnt % 2 == visited[2][j]:
        if check_valid(visited):
            result = 1
        return 0

    if all(cnt % 2 == visited[k][k] for k in range(3)):
        if check_valid(visited):
            result = 1
        return 0
    if all(cnt % 2 == visited[2 - k][k] for k in range(3)):
        if check_valid(visited):
            result = 1
        return 0
    return 1


def dfs(boards, visited, cnt):
    if check_valid(visited):
        return
    for i in range(3):
        for j in range(3):
            if boards[i][j] == check[cnt % 2] and visited[i][j] == -1:
                new_visited = copy.deepcopy(visited)
                new_visited[i][j] = cnt % 2
                if pre_win(new_visited, cnt, i, j) == 1:
                    dfs(boards, new_visited, cnt + 1)



def solution(board):
    visited = [[-1] * len(board) for i in range(len(board))]
    boards = []
    for element in board:
        boards.append(list(element))

    for i in range(3):
        for j in range(3):
            if boards[i][j] == ".":
                visited[i][j] = -2

    dfs(boards, visited, 0)
    return result


def main():
    print(solution(["OO.", "XXO", "XOX"]))


if __name__ == "__main__":
    main()
