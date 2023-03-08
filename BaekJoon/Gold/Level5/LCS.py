import sys

# dp 2차원 배열
def solution_case_one(str1, str2):
    dp = [[0]*(len(str2)+1) for i in range(len(str1)+1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(dp[-1][-1])

# dp 1차원 배열
def solution_case_two(str1, str2):
    dp = [0] * (len(str1) + 1)

    for i in range(1, len(str2) + 1):
        check = 0
        for j in range(1, len(str1) + 1):
            if check < dp[j]:
                check = dp[j]
            elif str1[j - 1] == str2[i - 1]:
                dp[j] = check + 1

    print(max(dp))



def main():
    str1 = sys.stdin.readline().rstrip()
    str2 = sys.stdin.readline().rstrip()
    # solution_case_one(str1, str2)
    solution_case_two(str1,str2)


if __name__ == '__main__':
    main()
