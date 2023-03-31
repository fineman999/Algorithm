import sys


def solution(N, p):
    p.sort()
    dp = [0]
    for i in range(N):
        dp.append(dp[-1] + p[i])
    return sum(dp)


def main():
    N = int(sys.stdin.readline().rstrip())
    p = list(map(int, sys.stdin.readline().rstrip().split()))

    print(solution(N, p))



if __name__ == '__main__':
    main()