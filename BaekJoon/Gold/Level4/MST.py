import sys
import heapq

parents = []
def find_parent(V):
    start = V
    while V != parents[V]:
        V = parents[V]
    parents[start] = V
    return V

def solution(V, E, heap):
    global parents
    parents = [i for i in range(V+1)]
    cnt = 0
    answer = 0
    while heap:
        (C, A, B) = heapq.heappop(heap)
        if find_parent(A) != find_parent(B):
            parents[find_parent(B)] = find_parent(A)
            cnt += 1
            answer += C
        if cnt == V:
            break
    return answer




def main():
    V, E = map(int, sys.stdin.readline().rstrip().split())
    heap = []
    for _ in range(E):
        A, B, C = map(int, sys.stdin.readline().rstrip().split())
        heapq.heappush(heap, (C, A, B))
    print(solution(V, E, heap))

if __name__ == '__main__':
    main()