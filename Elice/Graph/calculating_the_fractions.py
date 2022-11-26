import sys
from collections import deque

sys.setrecursionlimit(100000)
def BFS(graph,start,end):
    q = deque()
    global visited
    start_nodes = graph[start]
    visited[start] = 0
    for node in start_nodes:
        q.append(node)
        visited[node] = 1

    count = 2
    while q:
        popleft = q.popleft()

        start_nodes = graph[popleft]
        valid = False
        for node in start_nodes:
            if visited[node] == -1:
                q.append(node)
                visited[node] = visited[popleft]+1
                valid = True
        if valid:
            count += 1
    return visited[end]


def SNS(n_nodes, myInput, a, b):
    '''
    엘리스친구의 친구관계가 myInput으로 주어지고, 사용자 a, b가 주어질 때 둘 사이의 촌수를 반환합니다.
    '''
    if a==b: return 0
    global visited
    visited = [-1]*n_nodes
    start = a
    end = b
    graph = [[] for _ in range(n_nodes)]

    for i in range(len(myInput)):
        node_1, node_2 = myInput[i]
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)
    result_end = BFS(graph, start, end)

    return result_end

def main():

    n_nodes, m_edges = list(map(int, input().split()))
    a, b= map(int, input().split())

    myInput = []
    for i in range(m_edges):
        myInput.append(list(map(int,input().split())))
    print(SNS(n_nodes,myInput,a,b))

if __name__ == "__main__":
    main()