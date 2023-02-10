def dynamic_programming(money):
    if money[0] > money[1]:
        dp = [money[0], money[0]]
    else:
        dp = [money[0], money[1]]

    n = len(money)
    for i in range(2, n):
        dp.append(max(dp[-1], money[i] + dp[-2]))

    return dp[n-1]


def solution(money):
    if len(money) == 3:
        return max(money[0]+money[1], money[2])
    answer = max(dynamic_programming(money[1:]), dynamic_programming(money[:-1]))
    return answer

def main():
    print(solution([5, 2, 3, 5]))


if __name__ == "__main__":
    main()
