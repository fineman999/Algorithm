import sys
from collections import deque
result = 0

def left_graph(N, graph):
    global result
    new_graph = [[0]*N for _ in range(N)]
    for i in range(N):
        check = deque()
        valid = True
        for j in range(N):
            if graph[i][j] != 0:
                if not check:
                    check.append(graph[i][j])
                else:
                    if valid:
                        if check[-1] == graph[i][j]:
                            check.append(check.pop() + graph[i][j])
                            valid = False
                        else:
                            check.append(graph[i][j])
                            valid = True
                    else:
                        check.append(graph[i][j])
                        valid = True
        cnt = 0

        while check:
            ele = check.popleft()
            new_graph[i][cnt] = ele
            result = max(ele, result)
            cnt += 1
    if new_graph == graph:
        return new_graph, False
    return new_graph, True

def right_graph(N, graph):
    new_graph = [[0]*N for _ in range(N)]
    global result
    for i in range(N):
        check = deque()
        valid = True
        for j in range(N-1, -1, -1):
            if graph[i][j] != 0:
                if not check:
                    check.append(graph[i][j])
                else:
                    if valid:
                        if check[-1] == graph[i][j]:
                            check.append(check.pop()+ graph[i][j])
                            valid = False
                        else:
                            check.append(graph[i][j])
                            valid = True
                    else:
                        check.append(graph[i][j])
                        valid = True
        cnt = N-1
        while check:
            ele = check.popleft()
            new_graph[i][cnt] = ele
            result = max(ele, result)
            cnt -= 1
    if new_graph == graph:
        return new_graph, False
    return new_graph, True

def up_graph(N, graph):
    new_graph = [[0]*N for _ in range(N)]
    global result
    for i in range(N):
        check = deque()
        valid = True
        for j in range(N):
            if graph[j][i] != 0:
                if not check:
                    check.append(graph[j][i])
                else:
                    if valid:
                        if check[-1] == graph[j][i]:
                            check.append(check.pop()+ graph[j][i])
                            valid = False
                        else:
                            check.append(graph[j][i])
                            valid = True
                    else:
                        check.append(graph[j][i])
                        valid = True
        cnt = 0
        while check:
            ele = check.popleft()
            result = max(ele, result)
            new_graph[cnt][i] = ele
            cnt += 1
    if new_graph == graph:
        return new_graph, False
    return new_graph, True

def down_graph(N, graph):
    new_graph = [[0]*N for _ in range(N)]
    global result
    for i in range(N):
        check = deque()
        valid = True
        for j in range(N-1,-1,-1):
            if graph[j][i] != 0:
                if not check:
                    check.append(graph[j][i])
                else:
                    if valid:
                        if check[-1] == graph[j][i]:
                            check.append(check.pop()+ graph[j][i])
                            valid = False
                        else:
                            check.append(graph[j][i])
                            valid = True
                    else:
                        check.append(graph[j][i])
                        valid = True
        cnt = N-1
        while check:
            ele = check.popleft()
            result = max(ele, result)
            new_graph[cnt][i] = ele
            cnt -= 1
    if new_graph == graph:
        return new_graph, False
    return new_graph, True

def dfs(N, graph, valid, cnt):
    if not valid:
        return
    if cnt == 5:
        return
    # print("cnt", cnt)
    # for ele in graph:
    #     print(ele)
    # print()
    left, left_valid = left_graph(N, graph)
    dfs(N, left, left_valid, cnt + 1)

    right, right_valid = right_graph(N, graph)
    dfs(N, right, right_valid, cnt + 1)

    up, up_valid = up_graph(N, graph)
    dfs(N,  up, up_valid , cnt + 1)

    down, down_valid = down_graph(N, graph)
    dfs(N, down, down_valid, cnt + 1)



def solution(N, arr):
    global result
    result = max(map(max, arr))

    dfs(N, arr,True, 0)
    print(result)


def main():
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, arr)

if __name__ == '__main__':
    main()