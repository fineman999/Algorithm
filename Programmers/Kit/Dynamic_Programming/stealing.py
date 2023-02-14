def dynamic_programming(money):
    if money[0] > money[1]:
        dp = [money[0], money[0]]
    else:
        dp = [money[0], money[1]]

    for i in range(2, len(money)):
        dp.append(max(dp[-1], dp[-2] + money[i]))

    return dp[-1]

def solution(money):
    if len(money) == 3:
        return max(money[1], money[0] + money[2])
    return max(dynamic_programming(money[1:]), dynamic_programming(money[:-1]))

def main():
    print(solution([1, 2, 3]))


if __name__ == "__main__":
    main()
