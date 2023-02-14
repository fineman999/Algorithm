
result = 0
def dfs(numbers, target, now, cnt):
    if len(numbers) == cnt:
        if target == now:
            global result
            result += 1
        return
    dfs(numbers, target, now + numbers[cnt], cnt + 1)
    dfs(numbers, target, now - numbers[cnt], cnt + 1)


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return result



def main():
    print(solution(	[1, 1, 1, 1, 1], 3))


if __name__ == "__main__":
    main()
