import sys
from collections import deque
dx = [1,0,-1]
dy = [0,1,0]


def check_valid(graph, i, j, W):
    k = j - 1
    left = False
    while k >= 0:
        if graph[i][k] == 1:
            left = True
            break
        k -= 1

    k = j + 1
    right = False
    while k <= W - 1:
        if graph[i][k] == 1:
            right = True
            break
        k += 1
    if left and right:
        return True

    return False

def bfs(q, graph, H, W):
    cnt = 0
    while q:
        (x, y) = q.popleft()
        cnt += 1
        for i in range(3):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < ny < H and -1< nx < W and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((nx, ny))
    return cnt


def solution(H, W, graph):
    answer = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 0:
                if check_valid(graph, i, j, W):
                    q = deque()
                    q.append((j, i))
                    graph[i][j] = 1
                    answer += bfs(q, graph, H, W)
    print(answer)


def main():
    H, W = inputs()
    graph = [[0]*W for _ in range(H)]
    arr = list(inputs())
    for i in range(W):
        for j in range(arr[i]):
            graph[H-j-1][i] = 1
    solution(H, W, graph)


def solution2(H, W, arr):
    answer = 0
    for i in range(1, W-1):
        left = max(arr[:i])
        right = max(arr[i+1:])

        tmp = min(right, left)
        if arr[i] < tmp:
            answer += tmp - arr[i]

    print(answer)




def main2():
    H, W = inputs()
    arr = list(inputs())
    solution2(H, W, arr)

def inputs():
    return map(int, sys.stdin.readline().rstrip().split())


if __name__ == '__main__':
    # main()
    main2()