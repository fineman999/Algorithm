import sys

def solution(N):
    answer = [0, 1, 2]

    for i in range(3, N+1):
        answer.append((answer[-1] + answer[-2])%15746)

    return answer[N]

def main():
    N = int(sys.stdin.readline())
    print(solution(N))


if __name__ == "__main__":
    main()