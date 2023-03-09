import copy
import math
import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(graph, N, q, k):

    while q:
        (x,y) = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 <ny < N and -1< nx< N and graph[ny][nx] > k:
                graph[ny][nx] = -1
                q.append((nx, ny))



def solution(N, graph):
    max_water = 0
    min_water = math.inf
    for ele in graph:
        max_water = max(max_water, max(ele))
        min_water = min(min_water, min(ele))

    answer = 1
    for k in range(min_water, max_water+1):
        new_graph = copy.deepcopy(graph)
        sub_answer = 0
        for i in range(N):
            for j in range(N):
                if new_graph[i][j] > k:
                    q = deque()
                    q.append((j,i))
                    bfs(new_graph, N, q, k)
                    sub_answer += 1
                    # print(j,i, "k",k)

        # print(sub_answer)
        # print()
        answer = max(sub_answer, answer)

    print(answer)

def main():
    N = int(sys.stdin.readline())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    solution(N, graph)

if __name__ == '__main__':
    main()
