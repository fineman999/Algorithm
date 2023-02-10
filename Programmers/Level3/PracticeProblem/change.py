result = 0


def dfs(n, money, index):
    if n < 0:
        return
    elif n == 0:
        global result
        result += 1
        return
    else:
        for i in range(index, len(money)):
            index = i
            dfs(n-money[i], money, index)


def dynamic_programming(n: int, money: list):
    dp = [0]*(n + 1)
    dp[0] = 1
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i-coin]
    return dp[-1]


def solution(n, money):
    money.sort()
    answer = dynamic_programming(n,money)
    return answer

def main():
    print(solution(5, [1,2,5]))


if __name__ == "__main__":
    main()
