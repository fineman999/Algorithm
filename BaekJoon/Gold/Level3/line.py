import sys
import heapq

def solution(N, M, people):
    visited = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for a, b in people:
        graph[a].append(b)
        visited[b] += 1
    heap = []
    answer = ''
    for i in range(1, N+1):
        if visited[i] == 0:
            heapq.heappush(heap, i)
    while heap:
        node = heapq.heappop(heap)
        answer += str(node) + ' '
        for now in graph[node]:
            visited[now] -= 1
            if visited[now] == 0:
                heapq.heappush(heap, now)

    return answer





def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    people = []
    for _ in range(M):
        people.append(list(map(int, sys.stdin.readline().rstrip().split())))
    answer = solution(N, M, people)
    print(answer.rstrip())



if __name__ == '__main__':
    main()