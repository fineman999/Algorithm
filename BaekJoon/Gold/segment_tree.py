import copy
import math


def solution(n, samples):

    # 초기값
    graph, height, k = init(n, samples)

    # 구간 합 그래프 구하기
    prefix_sum_graph = copy.deepcopy(graph)
    prefix_sum(prefix_sum_graph, height)

    # 최대값 그래프 구하기
    max_graph = copy.deepcopy(graph)
    get_max(max_graph, height)

    # 최소값 그래프 구하기
    min_graph = copy.deepcopy(graph)
    get_min(min_graph, height)

    print(prefix_sum_graph)
    print(max_graph)
    print(min_graph)

    # 질의 값 2 ~ 6 까지의 값을 구하라
    points = [2, 6]
    start_index = int(math.pow(2, k)) + points[0] - 1
    end_index = int(math.pow(2, k)) + points[1] - 1

    prefix_sum_nodes = get_nodes(end_index, prefix_sum_graph, start_index)
    max_nodes = get_nodes(end_index, max_graph, start_index)
    min_nodes = get_nodes(end_index, min_graph, start_index)

    print(prefix_sum_nodes)
    print(max_nodes)
    print(min_nodes)

    # 데이터 업데이트 하기 5번째 인덱스를 10으로 업데이트 하기
    num = 10
    num_index = 5
    index = int(math.pow(2, k)) + num_index - 1
    print(index)
    update_prefix_graph(index, num, prefix_sum_graph)

    update_max_graph(index, max_graph, num)
    print(max_graph)
    update_min_graph(index, min_graph, num)
    print(min_graph)


def update_min_graph(index, min_graph, num):
    min_graph[index] = num
    while index > 0:
        if index % 2 == 0:
            min_graph[index // 2] = min(min_graph[index], min_graph[index + 1])
        else:
            min_graph[index // 2] = min(min_graph[index], min_graph[index - 1])
        index = index // 2


def update_max_graph(index, max_graph, num):
    max_graph[index] = num
    while index > 0:
        if index % 2 == 0:
            max_graph[index // 2] = max(max_graph[index], max_graph[index + 1])
        else:
            max_graph[index // 2] = max(max_graph[index], max_graph[index - 1])
        index = index // 2

def update_prefix_graph(index, num, prefix_sum_graph):
    check = num - prefix_sum_graph[index]
    while index > 0:
        prefix_sum_graph[index] += check
        index = index // 2
    print(prefix_sum_graph)


def get_nodes(end_index, graph, start_index):
    nodes = []
    while start_index <= end_index:
        if start_index % 2 == 1:
            nodes.append(graph[start_index])
        if end_index % 2 == 0:
            nodes.append(graph[end_index])

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2
    return nodes


def get_min(graph, height):
    for i in range(height - 1, 1, -1):
        if graph[i // 2] == 0:
            graph[i // 2] = graph[i]
        else:
            graph[i // 2] = min(graph[i], graph[i // 2])


def get_max(graph, height):
    for i in range(height - 1, 1, -1):
        graph[i // 2] = max(graph[i], graph[i // 2])


def prefix_sum(graph, height):
    for i in range(height - 1, 1, -1):
        graph[i // 2] += graph[i]



def init(n, samples):
    # 1. k 구하기
    k = math.ceil(math.log2(n))
    # 2. 높이 구하기
    height = int(math.pow(2, k) * 2)
    graph = [0 for _ in range(height)]
    # 3. 원본 데이터 입력하기
    start_index = int(math.pow(2, k))
    cnt = 0
    while cnt < len(samples):
        graph[start_index + cnt] = samples[cnt]
        cnt += 1
    return graph, height, k


def main():
    samples = [5, 8, 4, 3, 7, 2, 1, 6]
    n = len(samples)
    solution(n, samples)

if __name__ == '__main__':
    main()