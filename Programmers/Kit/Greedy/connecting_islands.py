
parents = []
def find_parents(node):
    while node != parents[node]:
        node = parents[node]
    return node

def solution(n, costs):

    # 정렬
    costs.sort(key=lambda x:x[2])
    global parents
    parents = [i for i in range(n)]
    # print(parents)
    answer = 0
    node_cnt = 1
    for start, end, weight in costs:
        if find_parents(start) != find_parents(end):
            parents[find_parents(end)] = find_parents(start)
            answer += weight
            node_cnt += 1
            if node_cnt == n:
                break

    return answer


def main():
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))


if __name__ == "__main__":
    main()