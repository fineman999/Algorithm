import copy
import math
import sys
from collections import deque
MAX_PRIME = 10_001
def find_prime(n):
    visited = [False]*n
    visited[0] = True
    visited[1] = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if not visited[i]:
            j = 2
            while j*i < n:
                visited[j*i] = True
                j += 1
    return visited



def bfs(q, end, visited):

    while q:
        (now, cnt) = q.popleft()
        if now == end:
            return cnt
        now = str(now)
        for i in range(4):
            for j in range(10):

                check = f'{now[:i]}{j}{now[i+1:]}'
                check = int(check)
                if check > 999 and not visited[check]:
                    visited[check] = True
                    q.append((check, cnt + 1))
    return 0


def solution(arr, visited):

    [start, end] = arr
    new_visited = copy.deepcopy(visited)
    new_visited[start] = True
    q = deque()

    q.append((start, 0))
    result = bfs(q, end, new_visited)

    return result



def main():
    T = int(sys.stdin.readline())
    answer = []
    visited = find_prime(MAX_PRIME)
    for _ in range(T):
        answer.append(solution(list(map(int, sys.stdin.readline().rstrip().split())), visited))

    for ele in answer:
        print(ele)


if __name__ == '__main__':
    main()