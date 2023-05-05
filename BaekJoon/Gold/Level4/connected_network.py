import sys
import heapq
parents = []


def set_parents(N):
    global parents
    parents = [i for i in range(N+1)]


def find_parent(node):
    start = node
    while parents[node] != node:
        node = parents[node]
    parents[start] = node
    return node


def sol(N, heap):
    global parents
    answer = 0
    cnt = 0
    while heap:
        weight, start, end = heapq.heappop(heap)
        parent_start = find_parent(start)
        parent_end = find_parent(end)
        if parent_start != parent_end:
            if parent_start > parent_end:
                parents[parent_end] = parent_start
            else:
                parents[parent_start] = parent_end
            answer += weight
            cnt += 1
            if cnt == N - 1:
                break
    return answer


def solution(N, heap):
    set_parents(N)

    answer = sol(N, heap)
    print(answer)


def main():
    N = input_number()
    M = input_number()
    heap = []
    for i in range(M):
        a,b,c = map(int, sys.stdin.readline().rstrip().split())
        heapq.heappush(heap, (c, a, b))
    solution(N, heap)


def input_number():
    return int(sys.stdin.readline().rstrip())


if __name__ == '__main__':
    main()
