import sys


def solution(M, N, K, menus, controls):
    if M > N:
        return "normal"

    for i in range(N):
        if controls[i] == menus[0]:
            try:
                if all(controls[i + j] == menus[j] for j in range(M)):
                    return "secret"
            except:
                continue
    return "normal"

    print(M, N, K, menus, controls)


def main():
    M, N, K = map(int, sys.stdin.readline().split())
    menus = list(map(int, sys.stdin.readline().split()))
    controls = list(map(int, sys.stdin.readline().split()))
    print(solution(M, N, K, menus, controls))


if __name__ == "__main__":
    main()