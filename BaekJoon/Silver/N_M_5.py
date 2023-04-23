import sys

answer = set()
def dfs(N, M, sequence, cnt, temp, visited):
    if M == cnt:
        tmp = ' '.join(map(str, temp))
        if tmp not in answer:
            print(tmp)
            answer.add(tmp)

        # print(*temp)
        return
    for i in range(N):
        if (not temp or temp[-1] <= sequence[i]):
            temp.append(sequence[i])
            # visited[i] = True
            dfs(N, M, sequence, cnt + 1, temp, visited)
            temp.pop()
            # visited[i] = False



def solution(N, M, sequence):
    sequence.sort()
    cnt = 0
    temp = []
    visited = [False]*N
    dfs(N, M, sequence, cnt, temp, visited)

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, M, sequence)


if __name__ == '__main__':
    main()