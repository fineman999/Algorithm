import sys
sys.setrecursionlimit(100000)

def getShortest(graph, start, end) :
    '''
    graph가 주어질 때, start부터 end까지의 최단거리를 반환하는 함수를 작성하세요.
    '''
    # 정점의 개수
    V = len(graph)

    # 각 정점의 거리
    dist = [float('inf') for i in range(V)]
    # 방문했는지 확인
    visited = [False for i in range(V)]

    dist[start] = 0

    while True:
        mini = float('inf')
        node = -1
        for j in range(V):
            if visited[j] == False and dist[j] < mini:
                mini = dist[j]
                node = j
        if mini == float('inf'):
            break
        visited[node] = True

        for j in range(len(graph[node])):
            des = graph[node][j][0]
            cost = graph[node][j][1]

            if dist[des] > dist[node] + cost:
                dist[des] = dist[node] + cost
    return dist[end]





    return graph

def main():
    vertexs, edges, start, end = map(int, input().split())
    graph = [ [] for i in range(vertexs) ]

    for i in range(edges) :
        line = [int(x) for x in input().split()]
        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))
    print(getShortest(graph,start,end))

if __name__ == "__main__":
    main()