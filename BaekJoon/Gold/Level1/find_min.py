import math
import sys


def get_node(start_index, end_index, graph):
    answer = math.inf
    while start_index <= end_index:
        if start_index % 2 == 1:
            answer = min(graph[start_index], answer)
        if end_index % 2 == 0:
            answer = min(graph[end_index], answer)
        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2
    return answer


def solution(N, M, arr, changes):

    graph, start_node = init(N, arr)

    for start_index, end_index in changes:
        answer = get_node(start_index + start_node - 1, end_index + start_node - 1, graph)
        print(answer)




def init(N, arr):
    # k 구하기
    k = math.ceil(math.log2(N))
    height = int(math.pow(2, k) * 2)
    graph = [0 for _ in range(height)]
    start_index = int(math.pow(2, k))

    for i in range(N):
        graph[start_index + i] = arr[i]
    for i in range(height -1 , 1, -1):
        if graph[i//2] == 0:
            graph[i//2] = graph[i]
        else:
            graph[i//2] = min(graph[i], graph[i//2])

    return graph, start_index


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for i in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))
    changes = []
    for i in range(M):
        changes.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, M, arr, changes)


if __name__ == '__main__':
    main()