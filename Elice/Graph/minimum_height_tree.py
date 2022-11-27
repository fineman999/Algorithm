import sys
sys.setrecursionlimit(100000)


def union_is_same_group(parent, a, b):
    parent_a = find(parent, a)
    parent_b = find(parent, b)
    if parent_a == parent_b:
        return True
    parent[b] = parent_a
    return False


def find(parent, a):
    if parent[a] == a:
        return a
    return find(parent, parent[a])


def getMST(graph) :
    '''
    graph가 주어질 때, 그 최소 비용 신장트리의 간선 가중치의 합을 반환하는 함수를 작성하세요.
    '''
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(len(graph[i])):
            neighbor = graph[i][j][0]
            cost = graph[i][j][1]
            edges.append([i, neighbor, cost])
    edges.sort(key=lambda edge: edge[2])
    m = len(edges)
    parent = [i for i in range(m)]

    result = 0
    for i in range(m):
        v1 = edges[i][0]
        v2 = edges[i][1]
        cost = edges[i][2]

        v1_parent = find(parent, v1)
        v2_parent = find(parent, v2)

        if not union_is_same_group(parent, v1_parent, v2_parent):
            result += cost
    return result


def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]

    graph = [ [] for i in range(n) ]

    for i in range(m) :
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))

    print(getMST(graph))

if __name__ == "__main__":
    main()