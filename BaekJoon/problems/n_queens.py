import math
import sys

result = 0


def dfs(N, depth, seq, visited):
    if N == depth:
        global result
        result += 1
        return
    for i in range(N):
        if not visited[i]:
            if not seq:
                visited[i] = True
                dfs(N, depth + 1, seq + [i], visited)
                visited[i] = False
            else:
                if not any(abs(index - depth) == abs(value - i)
                           for index, value in enumerate(seq)):
                    visited[i] = True
                    dfs(N, depth + 1, seq + [i],visited)
                    visited[i] = False


def solution(N):
    visited = [False]*N
    dfs(N, 0, [], visited)

    return result


def main():
    N = int(sys.stdin.readline())
    answer = solution(N)
    print(answer)


if __name__ == "__main__":
    main()
