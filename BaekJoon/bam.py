from collections import deque
import sys
# 북 , 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def solution(N, K, apples, L, direct):

    graph = [[0]*N for i in range(N)]
    for apple in apples:
        [row, column] = apple
        graph[row-1][column-1] = 1

    d = 1
    q = deque()
    q.append((0, 0))
    graph[0][0] = 2
    cnt = 0
    direct = deque(direct)

    while q:
        cnt += 1
        (x, y) = q.popleft()

        if not q:
            nx = x + dx[d]
            ny = y + dy[d]
        else:
            nx = q[-1][0] + dx[d]
            ny = q[-1][1] + dy[d]

        if -1 < ny < N and -1 < nx < N and graph[ny][nx] != 2:
            q.append((nx,ny))
            if graph[ny][nx] == 1:
                q.appendleft((x,y))
                graph[y][x] = 2
            graph[y][x] = 0
            graph[ny][nx] = 2
        else:
            break
        if direct and cnt == int(direct[0][0]):
            if direct[0][1] == "D":
                d = (d + 1)%4
            else:
                d = (d+3)%4
            direct.popleft()

    return cnt



def main():
    N = int(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline().rstrip())
    apples = []
    for i in range(K):
        apples.append(list(map(int, sys.stdin.readline().rstrip().split())))
    L = int(sys.stdin.readline().rstrip())
    direct = []
    for i in range(L):
        direct.append(list(sys.stdin.readline().rstrip().split()))

    print(solution(N, K, apples, L, direct))



if __name__ == "__main__":
    main()