import copy
import math
import sys


def inputs():
    return sys.stdin.readline().rstrip()


def init(n, nums):
    k = math.ceil(math.log2(n))
    height = int(math.pow(2, k) * 2)
    graph = [0 for _ in range(height)]
    start_index = int(math.pow(2, k))
    cnt = 0
    while cnt < len(nums):
        graph[start_index + cnt] = nums[cnt]
        cnt += 1
    return graph, height, k


def solution(N, nums, M, twins):
    graph, height, k = init(N, nums)
    max_graph = copy.deepcopy(graph)
    get_max_graph(max_graph, height)

    min_graph = copy.deepcopy(graph)
    get_min_graph(min_graph, height)


    for a, b in twins:
        start_index = int(math.pow(2, k)) + a - 1
        end_index = int(math.pow(2, k)) + b - 1
        max_answer = get_max_answer(end_index, max_graph, start_index)
        min_answer = get_min_answer(end_index, min_graph, start_index)
        print(min_answer, max_answer)


def get_max_answer(end_index, graph, start_index):
    check = 0
    while start_index <= end_index:
        if start_index % 2 == 1:
            check = max(check, graph[start_index])
        if end_index % 2 == 0:
            check = max(check, graph[end_index])

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2
    return check

def get_min_answer(end_index, graph, start_index):
    check = math.inf
    while start_index <= end_index:
        if start_index % 2 == 1:
            check = min(check, graph[start_index])
        if end_index % 2 == 0:
            check = min(check, graph[end_index])

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2
    return check

def get_min_graph(graph, height):
    for i in range(height - 1, 1, -1):
        if graph[i // 2] == 0:
            graph[i // 2] = graph[i]
        else:
            graph[i // 2] = min(graph[i], graph[i // 2])


def get_max_graph(graph, height):
    for i in range(height - 1, 1, -1):
        if graph[i] == 0:
            continue
        graph[i // 2] = max(graph[i], graph[i // 2])


def main():
    N, M = map(int, inputs().split())
    nums = []
    for _ in range(N):
        nums.append(int(inputs()))
    twins = []
    for _ in range(M):
        twins.append(list(map(int, inputs().split())))
    solution(N, nums, M, twins)

if __name__ == '__main__':
    main()

