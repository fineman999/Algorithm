import math

alphabets = [chr(i) for i in range(65, 91)]


def up_down(change_alphabet: str):
    up = 0
    for i in range(1, len(alphabets)):
        if alphabets[i] == change_alphabet:
            up = i
            break
    down = 0
    for i in range(1, len(alphabets)):
        if alphabets[-i] == change_alphabet:
            down = i
    return min(up, down)


result = math.inf


def dfs(start, visited, cnt):
    visited[start] = True
    if False not in visited:
        global result
        # print(visited)
        # print(cnt)
        result = min(result, cnt)
        return
    check = 1
    left = start - 1
    right = start + 1
    while check < len(visited):
        if left <= -len(visited):
            left = 0
        if right >= len(visited):
            right = 0
        if not visited[left]:
            dfs(left, visited, cnt + check)
        if not visited[right]:
            dfs(right, visited, cnt + check)
        check += 1
        left -= 1
        right += 1
    visited[start] = False


def solution(name):
    answer = 0
    start_name = 'A' * len(name)
    visited = [False] * len(name)
    for i in range(len(visited)):
        if name[i] == 'A':
            visited[i] = True
        else:
            answer += up_down(name[i])
    dfs(0, visited, 0)

    return answer + result


def main():
    print(solution("JAN"))


if __name__ == "__main__":
    main()
