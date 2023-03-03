import sys
# sys.setrecursionlimit(10**6)
NOT_VISITED = 0
VISITED = 1
CYCLE_IN = 2
NOT_CYCLE_IN = 3


def check(v, people, visited, stack):
    visited[v] = True
    stack.append(v)
    node = people[v]
    if visited[node]:
        if node in stack:
            return stack[stack.index(node):]
        return []
    return check(node,people,visited,stack)




def solution(N, people):
    visited = [False]*(N+1)
    cnt = 0

    for i in range(1, (N+1)):

        if not visited[i]:
            stack = []
            count = check(i, people, visited, stack)
            cnt += len(count)

    return N - cnt


def main():
    T = int(sys.stdin.readline())
    answer = []
    for i in range(T):
        N = int(sys.stdin.readline())
        arr = [0] + list(map(int, sys.stdin.readline().split()))
        answer.append(solution(N, arr))

    for ele in answer:
        print(ele)


if __name__ == "__main__":
    main()