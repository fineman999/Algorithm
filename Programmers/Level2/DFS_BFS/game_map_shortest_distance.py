from collections import deque


def direction(x,y,queue,maps):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(len(dx)):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < nx < len(maps[0]) and -1 < ny < len(maps):
            if maps[ny][nx] == 1:
                if ny == 0 and nx == 0:
                    continue
                # print(ny,nx)
                maps[ny][nx] = maps[y][x] + 1
                queue.append([nx,ny])
            elif maps[ny][nx] > maps[y][x] + 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append([nx,ny])
    return queue, maps



def bfs(queue, maps):

    while queue:
        popleft = queue.popleft()
        queue, maps = direction(popleft[0], popleft[1], queue, maps)
    return maps

def solution(maps):
    queue = deque()
    queue.append([0,0])
    maps = bfs(queue, maps)
    answer = maps[-1][-1]
    # print(maps)
    if answer == 1:
        return -1
    return answer


def main():
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))


if __name__ == "__main__":
    main()
