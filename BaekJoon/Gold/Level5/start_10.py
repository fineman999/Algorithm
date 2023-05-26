import sys


def dfs(i, j, N):
    if (i//N) % 3 == 1 and (j//N) % 3 == 1:
        print(" ", end="")
    else:
        if N//3 == 0:
            print("*", end="")
        else:
            dfs(i, j, N//3)

def star(N):
    if N == 1:
        return ["*"]
    temp = star(N//3)
    arr = []

    for s in temp:
        arr.append(s*3)
    for s in temp:
        arr.append(s + ' '*(N//3) + s)
    for s in temp:
        arr.append(s*3)
    return arr


def solution(N):
    temp = star(N)
    for ele in temp:
        print(ele)


def main():
    N = int(sys.stdin.readline().rstrip())

    solution(N)

if __name__ == '__main__':
    main()