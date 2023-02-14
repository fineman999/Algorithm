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
            break
    return min(up, down)


def dfs(start, visited, cnt):
    if False not in visited:
        return cnt

    answer = math.inf
    check = 1
    left = start - 1

    # 왼쪽으로 최소값
    while check < len(visited):
        if left <= -len(visited):
            left = 0
        if not visited[left]:
            visited[left] = True
            answer = min(dfs(left, visited, cnt + check), answer)
            visited[left] = False
            break
        check += 1
        left -= 1

    # 오른쪽으로 최소값
    check = 1
    right = start + 1
    while check < len(visited):
        if right >= len(visited):
            right = 0
        if not visited[right]:
            visited[right] = True
            answer = min(dfs(right, visited, cnt + check), answer)
            visited[right] = False
            break
        check += 1
        right += 1

    return answer


def solution(name):
    answer = 0
    visited = [False] * len(name)
    for i in range(len(visited)):
        if name[i] == 'A':
            visited[i] = True
        else:
            answer += up_down(name[i])
    visited[0] = True
    answer += dfs(0, visited, 0)

    return answer


def main():
    print(solution("BBBAAB"))


if __name__ == "__main__":
    main()
