import sys


def star(N):
    if N == 1:
        return [
            "*"
        ]
    temp = star(N//2)
    arr = []
    for ele in temp:
        print(ele)

    for s in temp:
        arr.append("  "*(N//2) + s + "  "*(N//2) + " "*(N//2))
    for s in temp:
        arr.append(" "*(N//2) + s + " "*(N//3) + s + " "*(N//2) + " "*(N//2))
    for s in temp:
        arr.append(s*5+ " "*(N//2))
    return arr


def solution(N):
    for i in range(1, N+1):
        print(" "*(N-i) + '*'*i)
    for i in range(N-1, 0, -1):
        print(" "*(N-i) + '*' * i)


def main():
    N = int(sys.stdin.readline().rstrip())
    solution(N)


if __name__ == '__main__':
    main()