import math
from collections import deque


def dfs(N, now, visited, number, cnt):
    if cnt > 8:
        print(now)
        visited[now] = -1
        return
    if now < 1:
        return

    if visited[now] < cnt:
        return

    visited[now] = cnt


    # 더하기

    dfs(N, now + N, visited, number, cnt + 1)
    # 빼기
    dfs(N, now - N, visited, number, cnt + 1)
    # 나누기
    dfs(N, now // N, visited, number, cnt + 1)
    if not all(str(N) == i for i in list(map(str,str(now)))):
        dfs(N, int(str(N)+str(now)), visited, number, cnt + 1)


def solution(N, number):
    answer = 0
    visited = [math.inf]*(32_001)
    visited[1] = 2
    visited[N] = 1
    arr = 123
    print(list(map(str,str(arr))))
    now = N
    dfs(N, now, visited, number, 1)
    print(visited)
    return answer

def main():
    print(solution(5,	12))


if __name__ == "__main__":
    main()
