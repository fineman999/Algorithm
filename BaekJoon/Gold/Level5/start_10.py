import sys


def dfs(i, j, N):
    if (i//N) % 3 == 1 and (j//N) % 3 == 1:
        print(" ", end="")
    else:
        if N//3 == 0:
            print("*", end="")
        else:
            dfs(i, j, N//3)


def solution(N):
    for i in range(N):
        for j in range(N):
            dfs(i, j, N)
        print()


def main():
    N = int(sys.stdin.readline().rstrip())

    solution(N)

if __name__ == '__main__':
    main()