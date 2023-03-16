import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
answer = 0


def dfs(now, diary, visited, depth):

    global answer
    [left, right] = diary[now]
    if left > -1 and not visited[left]:
        answer += 1
        dfs(left, diary, visited, depth + 1)
        answer += 1

    visited[now] = True
    del visited[now]
    if len(visited) == 0:
        # 깊이를 빼야지 해당 값이 나옴
        answer -= depth
        return

    if right > -1 and not visited[right]:
        answer += 1
        dfs(right, diary, visited, depth + 1)
        answer += 1

    if right == -1 and left == -1:
        return


def solution(N, graph):
    diary = defaultdict(list)
    visited = defaultdict(bool)
    for now, left, right in graph:
        diary[now] = [left, right]
        visited[now] = False

    dfs(1, diary, visited, 0)
    return answer

def main():
    N = int(sys.stdin.readline())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, graph))


if __name__ == '__main__':
    main()
