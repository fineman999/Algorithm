import copy
import sys
from collections import deque



def direction_j(x,y, q, graph, R, C):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 == ny or -1 == nx or ny == R or nx == C:
            return True

        if -1 < ny < R and -1 < nx < C and graph[ny][nx] == '.':
            graph[ny][nx] = 'J'
            q.append((nx, ny))
    return False


def direction_f(x,y, q, graph, R, C, new_j_q):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < ny < R and -1 < nx < C:
            if graph[ny][nx] == '.':
                graph[ny][nx] = 'F'
                q.append((nx, ny))
            elif graph[ny][nx] == 'J':
                if (nx, ny) in new_j_q:
                    new_j_q.remove((nx, ny))
                graph[ny][nx] = 'F'
                q.append((nx, ny))

def bfs(j_q, f_q, graph, R, C):
    answer = 0
    while j_q:
        answer += 1
        new_j_q = []
        while j_q:
            (x,y) = j_q.popleft()
            valid = direction_j(x, y, new_j_q, graph, R, C)
            if valid:
                return answer
        new_f_q = deque()
        while f_q:
            (f_x, f_y) = f_q.popleft()
            direction_f(f_x, f_y, new_f_q, graph, R, C, new_j_q)

        while new_j_q:
            j_q.append(new_j_q.pop())

        if new_f_q:
            f_q = copy.deepcopy(new_f_q)
        # for ele in graph:
        #     print(ele)
        # print()

    return "IMPOSSIBLE"



def solution(R, C, graph):
    j_q = deque()
    f_q = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'J':
                j_q.append((j,i))
            if graph[i][j] == 'F':
                f_q.append((j, i))

    answer = bfs(j_q, f_q, graph, R, C)
    print(answer)


def main():
    R, C = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for i in range(R):
        graph.append(list(sys.stdin.readline().rstrip()))
    solution(R, C, graph)

if __name__ == '__main__':
    main()
