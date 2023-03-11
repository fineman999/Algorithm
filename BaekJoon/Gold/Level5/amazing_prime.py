import math
import sys


# def get_prime(N):
#     visited = [False] * (10 ** N)
#     visited[0] = True
#     visited[1] = True
#     m = len(visited)
#     for i in range(2, int(math.sqrt(m)) + 1):
#         if not visited[i]:
#             j = 2
#             while j * i < m:
#                 visited[j * i] = True
#                 j += 1
#     return visited
def valid_prime(N):
    if N < 2:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N%i == 0:
            return False
    return True

answer = []
def dfs(N, cnt, result):
    if cnt == N:
        answer.append(result)
        return

    for j in range(10):
        if result == '':
            if valid_prime(j):
                dfs(N, cnt + 1, result + str(j))
        else:
            if valid_prime(int(f'{int(result)}{j}')):
                dfs(N, cnt + 1, result + str(j))



def solution(N):
    cnt = 0
    dfs(N, cnt, '')

    for ele in answer:
        print(ele)


def main():
    N = int(sys.stdin.readline())
    solution(N)


if __name__ == '__main__':
    main()
