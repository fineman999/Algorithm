import sys


def change_direcion(roads: list):
    arr = [0] * 101
    start = 0
    for road, vertex in roads:
        arr[start:start + road + 1] = [vertex] * (road)
        start += road

    return arr


def solution(N, M, roads, tests):
    roads = change_direcion(roads)
    tests = change_direcion(tests)
    answer = 0
    for i in range(100):
        answer = max(tests[i] - roads[i], answer)
    return answer


def main():
    N, M = map(int, sys.stdin.readline().split())
    roads = []
    tests = []
    for i in range(N):
        roads.append(list(map(int, sys.stdin.readline().split())))
    for i in range(M):
        tests.append(list(map(int, sys.stdin.readline().split())))
    answer = solution(N, M, roads, tests)
    print(answer)


if __name__ == "__main__":
    main()