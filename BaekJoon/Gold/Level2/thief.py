import sys
import heapq


def solution(N, products, K, weights):
    heap = []

    weights.sort()
    products.sort()
    # print(weights, products)
    answer = 0
    for weight in weights:
        while products and products[0][0] <= weight:
            heapq.heappush(heap, -heapq.heappop(products)[1])
        if heap:
            answer -= heapq.heappop(heap)

    return answer


def main():
    N, K = map(int,sys.stdin.readline().rstrip().split())
    products = []
    for i in range(N):
        products.append(list(map(int, sys.stdin.readline().rstrip().split())))
    weights = []
    for i in range(K):
        weights.append(int(sys.stdin.readline()))

    print(solution(N, products, K, weights))

if __name__ == '__main__':
    main()
