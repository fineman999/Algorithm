import math
import sys

def init(n, arr):
    k = math.ceil(math.log2(n))
    cal = math.pow(2, k)
    height = int(cal * 2)
    graph = [0 for _ in range(height)]

    start_index = int(cal)
    cnt = 0
    while cnt < n:
        graph[start_index + cnt] = arr[cnt]
        cnt += 1
    return graph, height, k

def make_prefix_sum(graph, height):
    for i in range(height - 1, 1, -1):
        graph[i // 2] += graph[i]


def update_prefix_sum(index, num, graph):
    check = num - graph[index]

    while index > 0:
        graph[index] += check
        index = index // 2


def print_prefix_sum(start_index, end_index, graph):
    answer = 0
    while start_index <= end_index:
        if start_index % 2 == 1:
            answer += graph[start_index]
        if end_index % 2 == 0:
            answer += graph[end_index]

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2
    return answer



def solution(N, M, K, arr, changes):
    graph, height, j = init(N, arr)
    cal = int(math.pow(2, j))
    # print(cal)
    make_prefix_sum(graph, height)
    # print(graph)
    for types, start, end in changes:
        if types == 1:
            index = cal + start - 1
            update_prefix_sum(index, end, graph)
            # print(graph)
        else:
            start_index = cal + start - 1
            end_index = cal + end - 1
            answer = print_prefix_sum(start_index, end_index, graph)
            print(answer)


def main():
    N, M, K = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for i in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))
    changes = []
    for i in range(M+K):
        changes.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, M, K, arr, changes)


if __name__ == '__main__':
    main()
