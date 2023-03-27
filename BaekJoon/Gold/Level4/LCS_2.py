import sys


def solution(str1, str2):
    dp = [[] for _ in range(len(str1))]
    answer = 0
    result = ''
    for i in range(len(str2)):
        check = ''
        for j in range(len(str1)):
            if len(check) < len(dp[j]):
                check = dp[j]
            else:
                if str2[i] == str1[j]:
                    if len(dp[j]) < len(check + str1[j]):
                        dp[j] = check + str1[j]

    for i in range(len(dp)):
        if answer < len(dp[i]):
            answer = len(dp[i])
            result = dp[i]

    print(answer)
    print(result)




def main():
    str1 = sys.stdin.readline().rstrip()
    str2 = sys.stdin.readline().rstrip()
    solution(str1, str2)


if __name__ == '__main__':
    main()