import math
from collections import deque
result = math.inf


dp = []


def bfs(x, y, n):
    q = deque()
    global dp
    dp[x] = 0
    q.append([x, dp[x]])

    while q:

        [x, cnt] = q.popleft()
        if x < y:
            cnt += 1
            if x + n <= y and (dp[x + n] == math.inf or cnt < dp[x + n]):
                dp[x+n] = cnt
                q.append([x + n, cnt])
            if x * 2 <= y and (dp[x * 2] == math.inf or cnt < dp[x * 2]):
                dp[x * 2] = cnt
                q.append([x * 2, cnt])
            if x * 3 <= y and (dp[x * 3] == math.inf or cnt < dp[x * 3]):
                dp[x * 3] = cnt
                q.append([x * 3, cnt])


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