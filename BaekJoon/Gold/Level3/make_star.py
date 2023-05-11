import math
import sys
import heapq

parents = []


def get_parent(node):
    start = node
    while node != parents[node]:
        node = parents[node]
    parents[start] = node
    return node


def solution(N, points):
    heap = []
    global parents
    parents = [i for i in range(N + 1)]
    for i in range(N):
        a1, b1 = points[i]
        for j in range(i + 1, N):
            a2, b2 = points[j]
            heapq.heappush(heap, (math.sqrt(abs(a1 - a2) ** 2 + abs(b1 - b2) ** 2), i + 1, j + 1))
    answer = 0
    cnt = 0
    while heap:
        dist, a, b = heapq.heappop(heap)
        parent_a = get_parent(a)
        parent_b = get_parent(b)
        if parent_b != parent_a:
            cnt += 1
            if parent_a > parent_b:
                parents[parent_b] = parent_a
            else:
                parents[parent_a] = parent_b
            answer += dist
        if cnt == N:
            break

    print(round(answer, 2))


def main():
    N = int(sys.stdin.readline().rstrip())
    points = []
    for _ in range(N):
        points.append(list(map(float, sys.stdin.readline().rstrip().split())))
    solution(N, points)


if __name__ == '__main__':
    main()
