import copy

result = []
max_result = 0
origin_n = 0


def calculate(info, visited):
    aphche = 0
    lion = 0
    for i in range(11):
        if info[i] == 0 and visited[i] == 0:
            continue
        if info[i] >= visited[i]:
            aphche += 10 - i
        else:
            lion += 10 - i
    return aphche, lion
def dfs(n, info, visited, cnt):
    if n == 0 and sum(visited) == origin_n:
        (aphche, lion) = calculate(info, visited)

        if lion > aphche:
            global max_result
            global result
            if not result:
                result = visited
                max_result = lion - aphche
                return
            if max_result == lion - aphche:
                for i in range(10, -1, -1):
                    if visited[i] == result[i]:
                        continue
                    if visited[i] > result[i]:
                        result = visited
                        max_result = lion - aphche
                        break
                    else:
                        break
            elif max_result < lion - aphche:
                result = visited
                max_result = lion -aphche
                return
        return

    for i in range(cnt, len(info) - 1):
        if info[i] + 1 <= n:
            new_visited = copy.deepcopy(visited)
            new_visited[i] = info[i] + 1
            dfs(n - info[i] - 1, info, new_visited, i)

    if n > 0:
        new_visited = copy.deepcopy(visited)
        new_visited[10] = n
        dfs(0, info, new_visited, i)


def solution(n, info):
    answer = []
    visited = [0] * 11
    global origin_n
    origin_n = n
    dfs(n, info, visited, 0)

    if result == []:
        return [-1]
    return result


def solution(n, info):
    answer = []
    visited = [0] * 11
    global origin_n
    origin_n = n
    dfs(n, info, visited, 0)

    if result == []:
        return [-1]
    return result
def main():
    print(solution(	5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))


if __name__ == "__main__":
    main()