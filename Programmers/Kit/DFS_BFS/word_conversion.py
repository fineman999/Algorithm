import math


def valid_change_word(now: str, word:str):
    cnt = 0
    for i in range(len(word)):
        if word[i] != now[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False


def dfs(begin, target, words, visited, cnt):
    if begin == target:
        return cnt
    result = math.inf
    for i in range(len(words)):
        if not visited[i] and valid_change_word(begin, words[i]):
            visited[i] = True
            result = min(result, dfs(words[i], target, words, visited, cnt + 1))
            visited[i] = False
    return result


def solution(begin, target, words):
    visited = [False]*len(words)
    result = dfs(begin, target, words, visited, 0)

    if result == math.inf:
        return 0
    return result

def main():
    print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log"]))


if __name__ == "__main__":
    main()
