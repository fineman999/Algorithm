def solution(board):
    answer = 0
    if len(board) == 1:
        return 1
    for i in range(1, len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1:
                board[i][j] += min(board[i-1][j-1], board[i][j-1], board[i-1][j])
                answer = max(answer, board[i][j]**2)
    return answer


def main():

    return print(solution([[0, 1, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]))


if __name__ == "__main__":
    main()
