import sys
import heapq

def solution(N, graph, topology):
    heap = []
    tmp = 0
    while True:
        for i in range(1, N+1):
            if topology[i] == tmp:
                heapq.heappush(heap, i)
        if heap:
            break
        tmp += 1
    answer = []
    while heap:
        node = heapq.heappop(heap)
        answer.append(node)
        for now in graph[node]:
            topology[now] -= 1
            if topology[now] == tmp:
                heapq.heappush(heap, now)
    if len(answer) == N:
        for ele in answer:
            print(ele)
    else:
        print(0)





def main():
    N, M = inputs()
    graph = [[] for _ in range(N+1)]
    topology = [0]*(N+1)
    for _ in range(M):
        tmp = list(inputs())
        for i in range(2, len(tmp)):
            graph[tmp[i-1]].append(tmp[i])
            topology[tmp[i]] += 1
    solution(N, graph, topology)


def inputs():
    return map(int, sys.stdin.readline().rstrip().split())

if __name__ == '__main__':
    main()
