import sys
import heapq

parents = []

def find_parents(node):
    start = node
    while parents[node] != node:
        node = parents[node]
    parents[start] = node
    return node


def solution(N, well, arr):
    global parents
    parents = [i for i in range(N+1)]
    graph = []

    for i,value in enumerate(well):
        heapq.heappush(graph,(value, 0, i+1))

    for i in range(N):
        for j in range(i+1, N):
            heapq.heappush(graph,(arr[i][j], i+1, j+1))


    answer = 0
    node_cnt = 1
    while graph:
        (weight, start, end) = heapq.heappop(graph)
        if find_parents(start) != find_parents(end):
            parents[find_parents(end)] = find_parents(start)
            answer += weight
            node_cnt += 1
            if node_cnt == N+1:
                break
    print(answer)


def main():
    N = int(sys.stdin.readline().rstrip())
    well = []
    for _ in range(N):
        well.append(int(sys.stdin.readline().rstrip()))
    graph = []
    for _ in range(N):
        graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    solution(N, well, graph)

if __name__ == '__main__':
    main()
