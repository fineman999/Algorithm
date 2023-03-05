import copy
import math
from collections import deque
from itertools import combinations
import sys





def solution(N, M, graph):
    combi = []
    house = []
    answer = math.inf
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                combi.append((j,i))
            if graph[i][j] == 1:
                house.append((j, i))
    for element in combinations(combi, M):
        cnt = 0
        for dx, dy in house:
            count = math.inf
            for x, y in element:
                check = abs(x - dx) + abs(y - dy)
                if check < count:
                    count = check
            cnt += count

        answer = min(answer, cnt)

    return answer

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    print(solution(N, M, graph))



if __name__ == "__main__":
    main()