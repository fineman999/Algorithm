import copy
import math
import sys

def check_graph(graph: list, n, x, y):
    cnt_y = 0
    while cnt_y < n:
        cnt_x = 0
        tmp = x
        while cnt_x < n:
            if graph[y][tmp] == 0:
                return False
            tmp -= 1
            cnt_x += 1
        y -= 1
        cnt_y += 1
    return True

def change_graph(graph: list, n, x, y):
    cnt_y = 0
    while cnt_y < n:
        cnt_x = 0
        tmp = x
        while cnt_x < n:
            graph[y][tmp] = 0
            tmp -= 1
            cnt_x += 1
        y -= 1
        cnt_y += 1
def back_graph(graph: list, n, x, y):
    cnt_y = 0
    while cnt_y < n:
        cnt_x = 0
        tmp = x
        while cnt_x < n:
            graph[y][tmp] = 1
            tmp -= 1
            cnt_x += 1
        y -= 1
        cnt_y += 1



def recursive(x, y, graph, cnt, dp):

    result = math.inf
    for i in range(y, -1, -1):
        for j in range(9, -1, -1):
            if graph[i][j] > 0 and cnt + 1:
                # print(j, i)
                for k in range(5, 0, -1):
                    if dp[k] > 0 and check_graph(graph, k, j, i):
                        # print(k, j, i, dp)
                        change_graph(graph, k, j, i)
                        dp[k] -= 1
                        result = min(result,recursive(j, i, graph, cnt + 1, dp))
                        dp[k] += 1
                        back_graph(graph, k, j, i)
                if result > 0:
                    # print(result)
                    return result
                else:
                    return -1
    for ele in graph:
        if any(i > 0 for i in ele):
            return math.inf
    return cnt


def solution(graph):

    dp = [0, 5, 5, 5, 5, 5]

    answer = recursive(9, 9, graph, 0, dp)
    if answer == math.inf:
        return -1
    return answer



def main():
    graph = []
    for _ in range(10):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(graph))

if __name__ == '__main__':
    main()