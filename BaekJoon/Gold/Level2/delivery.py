import sys
from collections import defaultdict

def solution(N, C, M, delivery):
    country = [C]*(N+1)

    delivery.sort(key=lambda x: (x[1], x[0]))
    answer = 0
    for start, end, weight in delivery:
        check = min(country[start:end])
        if check == 0:
            continue
        if weight >= check:
            for i in range(start, end):
                country[i] -= check
            answer += check
        elif weight < check:
            for i in range(start, end):
                country[i] -= weight
            answer += weight
        # print(country)
    return answer




def main():
    N, C = map(int, sys.stdin.readline().rstrip().split())
    M = int(sys.stdin.readline().rstrip())
    delivery = []
    for _ in range(M):
        delivery.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, C, M, delivery))


if __name__ == '__main__':
    main()