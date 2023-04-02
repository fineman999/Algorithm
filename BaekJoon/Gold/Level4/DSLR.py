import sys
from collections import deque



def bfs(A, B, visited):
    q = deque()
    q.append((A, ''))
    # global visited
    count = ''
    while q:
        (num, cnt) = q.popleft()
        visited[num] = 1
        if num == B:
            count = cnt
            break
        # D
        if 2*num < 10_000 and visited[2*num] == 0:
            visited[2*num] = 1
            q.append((2*num, cnt+'D'))
        if 2*num > 9999 and visited[(2*num)%10_000] == 0:
            visited[(2*num)%10_000] = 1
            q.append(((2*num)%10_000, cnt + 'D'))
        # S

        if num > 0 and visited[num - 1] == 0:
            visited[num-1] = 1
            q.append((num-1, cnt+'S'))
        if num < 1 and visited[9999] == 0:
            visited[9999] = 1
            q.append((9999, cnt + 'S'))

        # L
        L_move = int((num % 1000) * 10 + num / 1000)
        if visited[L_move] == 0:
            visited[L_move] = 1
            q.append([L_move, cnt+"L"])

        R_move = int((num % 10) * 1000 + num / 10)
        if visited[R_move] == 0:
            visited[R_move] = 1
            q.append([R_move, cnt + "R"])

    return count

def solution(arr):
    A, B = arr

    visited = [0 for _ in range(10000)]
    left = bfs(A, B, visited)
    print(left)




def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        solution(list(map(int, sys.stdin.readline().rstrip().split())))


if __name__ == '__main__':
    main()