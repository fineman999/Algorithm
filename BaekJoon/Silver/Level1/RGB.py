import math
import sys
def solution(N, house):
    answer = [house[0]]

    for i in range(1, N):
        [R, G, B] = house[i]
        answer.append([R + min(answer[i - 1][1], answer[i - 1][2]),
                       G + min(answer[i - 1][0], answer[i - 1][2]),
                       B + min(answer[i - 1][0], answer[i - 1][1])])

    return min(answer[N - 1])

def main():
    N = int(sys.stdin.readline())
    house = []
    for i in range(N):
        house.append(list(map(int, sys.stdin.readline().split())))

    print(solution(N, house))


if __name__ == "__main__":
    main()
