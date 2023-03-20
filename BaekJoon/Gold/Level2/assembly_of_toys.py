import sys
from collections import deque
import heapq
def solution(N, M, parts):
    visited = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    # 1. 그래프 생성을 노드에 (서브 노드, 해당 요소를 가기 위한 가중치) 저장
    # 2. 해당 간선의 개수를 서브 노드에 저장
    for part, sub_part, cnt in parts:
        graph[part].append((sub_part, cnt))
        visited[sub_part] += 1
    heap = []

    # 루트 노드를 힙에 저장
    heapq.heappush(heap, (N, 1))
    # 가기 위한 가중치 초기값
    basic_parts = [0]*(N+1)
    # print(basic_parts)

    # 6. 간선의 개수가 모두 0이 될 때까지 반복
    while heap:
        (target, cnt) = heapq.heappop(heap)
        for i in range(len(graph[target])):
            (v, now_cnt) = graph[target][i]
            # print(v, now_cnt, target, cnt)
            # 3. target 노드로 가기 위한 가중치 값과 현재 노드의 가중치를 곱함
            basic_parts[v] += now_cnt * cnt
            # 4. 완료 후 해당 간선 -1
            visited[v] -= 1
            # 5. 만약 해당 간선을 모두 완료 할 경우,
            # 해당 노드에서 루트 노드까지의 갈 수 있는 가중치를 모두 구했으므로 해당 큐에 저장
            if visited[v] == 0:
                heapq.heappush(heap, (v, basic_parts[v]))

    for i in range(1, N):
        if not graph[i]:
            print(f"{i} {basic_parts[i]}")



def main():
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    parts = []
    for _ in range(M):
        parts.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, M, parts)

if __name__ == '__main__':
    main()
