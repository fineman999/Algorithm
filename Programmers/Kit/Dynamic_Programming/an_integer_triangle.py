def solution(triangle):

    dp = [[triangle[0][0]]]
    for i in range(1, len(triangle)):
        check_dp = []

        for j in range(len(triangle[i])):
            if j == 0:
                check_dp.append(triangle[i][j] + dp[i-1][0])
            elif j == len(triangle[i]) - 1:
                check_dp.append(triangle[i][j] + dp[i-1][-1])
            else:
                check_dp.append(triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j]))
        dp.append(check_dp)

    return max(dp[-1])

def main():
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


if __name__ == "__main__":
    main()
