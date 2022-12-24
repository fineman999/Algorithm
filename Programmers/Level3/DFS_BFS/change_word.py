from collections import deque

def bfs(queue, target, words, visited, cnt):
    try:
        queue_pop = queue.pop()

        if queue_pop == target:
            return cnt

        for i in range(len(words)):
            if visited[i]:
                continue
            count = 0
            for j in range(len(words[i])):
                if words[i][j] != queue_pop[j]:
                    count += 1
            if count == 1:
                queue.append(words[i])
                visited[i] = True
        return bfs(queue, target, words, visited, cnt + 1)
    except:
        return 0


def solution(begin, target, words):
    visited = [False]*len(words)
    queue = deque()

    for i in range(len(words)):
        if visited[i]:
            continue
        count = 0
        for j in range(len(words[i])):
            if words[i][j] != begin[j]:
                count += 1
        if count == 1:
            queue.append(words[i])
            visited[i] = True
    if not queue:
        return 0
    return bfs(queue, target, words, visited, 1)


def main():
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


if __name__ == "__main__":
    main()
