import sys


def dfs(N, M, sequence, cnt, temp):
    if M == cnt:
        print(*temp)
        return
    for i in range(N):
        # if sequence[i] not in temp:
        if not temp or temp[-1] <= sequence[i]:
            temp.append(sequence[i])
            dfs(N, M, sequence, cnt + 1, temp)
            temp.remove(sequence[i])



def solution(N, M, sequence):
    sequence.sort()
    cnt = 0
    temp = []
    dfs(N, M, sequence, cnt, temp)


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, M, sequence)


if __name__ == '__main__':
    main()