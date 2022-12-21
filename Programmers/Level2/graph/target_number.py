def solution(numbers, target):

    return dfs(numbers, 0, 0, target)

def dfs(numbers, result, cnt, target):
    if len(numbers) == cnt:
        if result == target:
            return 1
        return 0
    return dfs(numbers, result - numbers[cnt], cnt + 1, target) + dfs(numbers, result + numbers[cnt], cnt + 1, target)


def main():
    print(solution([1, 1, 1, 1, 1], 3))


if __name__ == "__main__":
    main()
