import math
from collections import deque
dp = []


def bfs(x, y, n):
    q = deque()
    global dp
    dp[x] = 0
    q.append(x)
    while q:
        x = q.popleft()
        if x < y:
            if x + n <= y and (dp[x + n] == math.inf or dp[x] + 1 < dp[x + n]):
                dp[x + n] = dp[x] + 1
                q.append(x + n)
            if x * 2 <= y and (dp[x * 2] == math.inf or dp[x] + 1 < dp[x * 2]):
                dp[x * 2] = dp[x] + 1
                q.append(x * 2)
            if x * 3 <= y and (dp[x * 3] == math.inf or dp[x] + 1 < dp[x * 3]):
                dp[x * 3] = dp[x] + 1
                q.append(x * 3)


def solution(x, y, n):
    if x == y:
        return 0

    global dp
    dp = [math.inf]*(y+1)
    bfs(x, y, n)
    if dp[y] == math.inf:
        return -1
    return dp[y]

def main():
    print(solution(10,	40,	5))


if __name__ == "__main__":
    main()