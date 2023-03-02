

def solution(board, skill):
    M = len(board)
    N = len(board[0])
    dp = [[0] * (N+1) for i in range(M+1)]
    types = [0, -1, 1]
    for index, y1, x1, y2, x2, degree in skill:
        dp[y1][x1] += degree*types[index]
        dp[y1][x2+1] += degree*types[index]*-1

        dp[y2+1][x1] += degree*types[index]*-1
        dp[y2+1][x2+1] += degree*types[index]
        # for i in dp:
        #     print(i)
        # print()

    for i in range(M+1):
        for j in range(1, N+1):
            dp[i][j] += dp[i][j-1]
    for i in range(N+1):
        for j in range(1, M +1):
            dp[j][i] += dp[j-1][i]
    answer = 0
    for i in range(M):
        for j in range(N):
            board[i][j] += dp[i][j]
            if board[i][j] > 0:
                answer += 1
    # for i in board:
    #     print(i)
    return answer



def main():
    print(solution(	[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))


if __name__ == "__main__":
    main()